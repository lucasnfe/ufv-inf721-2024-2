var w = 840;
var h = 400;
var scl = 25;

let init = null;
let snake = null;
let food = null;

let isGameOver = false;
let isLearning = false;
let isExperiment = false;

let episodeActions = 0;
let maxActions = 1000;

let empty = [];
let walls = {};

var experiments_amount = 30;
let experiments_marks = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192];
let experiment_scores = [];
let experiment_data = [];

// Connect to WebSocket server
const socket = io('http://localhost:5001');

// Event listener for when the connection is established
socket.on('connect', function () {
    console.log('Connected to WebSocket server');
});

// Event listener for incoming messages
socket.on('message_from_server', function (message) {    
    if (message['type'] == "action") {
        if(message['action'] != null && (isLearning  || isExperiment)) {
            action = message['action'];
            actionResponse(action);
        }
    }
});

function saveResults() {
    print(experiment_data)

    // Construct the URL with the experiments data as a query parameter
    var url = 'http://localhost:5001/save_results?results=' + JSON.stringify(experiment_data);

    // Make a GET request to the server
    fetch(url)
    .then(response => response.json())
    .then(data => {
        // Process the response from the server
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function actionResponse(action) {
    episodeActions++;

    applyAction(action);
    snake.update();

    let sleepTime = document.getElementById('sleep').value * 1000;

    // Sleep for 1 second before sending the next action
    setTimeout(function() {
        // Get map
        let map = worldToMap();
        
        // Get snake position
        let snakePos = [snake.x, snake.y];

        // Get tail 
        let tailPos = [];
        for(let i = 0; i < snake.tail.length; i++) {
            tailPos.push([snake.tail[i].x, snake.tail[i].y]);
        }

        // Get food position
        let foodPos = [food.x, food.y];

        let qEpsilon = parseFloat(document.getElementById('epsilon').innerHTML);
        let qAlpha = document.getElementById('alpha').value;
        let qGamma = document.getElementById('gamma').value;

        let msg_type = "q_update";
        if (isExperiment) {
            msg_type = "q_experiment";
        }

        socket.emit('message_from_client',  {"type": msg_type, 
                                              "map": map, 
                                             "head": snakePos,
                                             "tail": tailPos,
                                             "food": foodPos,
                                          "epsilon": qEpsilon, 
                                            "alpha": qAlpha, 
                                            "gamma": qGamma});
        if (snake.eat(food)) {
            episodeActions = 0;
            
            // Increase point
            let score = parseInt(document.getElementById('score').innerHTML);
            score++;
            document.getElementById('score').innerHTML = score;

            // Pick new location for food
            pickLocation(empty);
        }                                                    

        if (snake.death() || episodeActions > maxActions) {
            if (!isExperiment) {
                // Update episode count
                let episodeCount = parseInt(document.getElementById('episodes').innerHTML);
                episodeCount++;
                document.getElementById('episodes').innerHTML = episodeCount;
                
                // Update epsilon
                updateEpsilon();

                // Run experiment
                if (experiments_marks.includes(episodeCount)) {
                    // Run 30 episodes and collect the final score
                    experiment_scores = [];
                    isLearning = false;
                    isExperiment = true;
                }
            } 
            else {
                if (experiment_scores.length < experiments_amount) {
                    let score = parseInt(document.getElementById('score').innerHTML);
                    experiment_scores.push(score);

                    // Update experiment count
                    let experimentCount = parseInt(document.getElementById('experiments').innerHTML);
                    experimentCount++;
                    document.getElementById('experiments').innerHTML = experimentCount;
                }
                else {
                    // Finish experiment
                    experiment_data.push(experiment_scores);
                    isLearning = true;
                    isExperiment = false;

                    document.getElementById('experiments').innerHTML = 0;
                    saveResults();
                }
            }

            isGameOver = false;
            episodeActions = 0;

            // Reset score
            document.getElementById('score').innerHTML = 0;

            // Restart game
            snake = new Snake();
            snake.x = init.x;
            snake.y = init.y;
            
            pickLocation(empty);
        }

    }, sleepTime);
}

function startSearch() { 
    // Get map  
    let map = worldToMap();

    // Get snake 
    let snakePos = [snake.x, snake.y];
    
    let tailPos = [];
    for(let i = 0; i < snake.tail.length; i++) {
        tailPos.push([snake.tail[i].x, snake.tail[i].y]);
    }

    // Get food 
    let foodPos = [food.x, food.y];

    let qEpsilon = parseFloat(document.getElementById('epsilon').innerHTML);
    let qAlpha = document.getElementById('alpha').value;
    let qGamma = document.getElementById('gamma').value;

    // Construct the URL with parameters
    var url = `http://localhost:5001/start_search?map=${encodeURIComponent(map)}&head=${encodeURIComponent(snakePos)}&tail=${encodeURIComponent(tailPos)}&food=${encodeURIComponent(foodPos)}&epsilon=${qEpsilon}&alpha=${qAlpha}&gamma=${qGamma}`;

    // Make a GET request to the server
    fetch(url)
    .then(response => response.json())
    .then(data => {
        // Process the response from the server
        action = data.action;
        actionResponse(action);
    })
    .catch(error => {
        console.error('Error:', error);
    });

    // Disable button
    document.getElementById('startSearch').disabled = true;

    // Enable save button
    document.getElementById('saveResults').disabled = false;

    isLearning = true;
}

function updateEpsilon() {
    let epsilonMax = parseFloat(document.getElementById('epsilonMax').value);
    let epsilonMin = parseFloat(document.getElementById('epsilonMin').value);
    let lambda = parseFloat(document.getElementById('lambda').value);
    let episodeCount = parseFloat(document.getElementById('episodes').innerHTML);

    // Update epsilon value using exponential decay
    let epsilon = epsilonMin + (epsilonMax - epsilonMin) * Math.exp(-lambda * episodeCount);    
    document.getElementById('epsilon').innerHTML = epsilon;
}

function preload() {
    getMaps();
}

function setup() {
    // Create canvas
    let mapCanvas = createCanvas(w, h);
    mapCanvas.parent("mapCanvas");

    // Config inputs
    document.getElementById('epsilonMax').value = 1.0;
    document.getElementById('epsilonMin').value = 0.001;
    document.getElementById('lambda').value = 0.001;
    document.getElementById('alpha').value = 0.1;
    document.getElementById('gamma').value = 0.9;
    document.getElementById('sleep').value = 0;
    document.getElementById('epsilon').innerHTML = 0.8;
    
    // Init world
    startMap();

    let mapSelect = document.getElementById('maps');
    mapSelect.addEventListener('change', function() {
        let selectedMap = this.value;
        if(selectedMap != '') {
            loadMap(selectedMap);
        }
        else {
            updateMapSize();
        }
    });

    frameRate(8)
}

//function to store snake's location on the grid
//floor calculates the closest int value that is less than or equal to the value of the parameter.
function pickLocation(empty) {
    food_position = empty[Math.floor((Math.random()*empty.length))]
    food = createVector(food_position[0], food_position[1]);
}

function applyAction(action) {
    if(action == 'w') {
        if(snake.yspeed != 1)
            snake.dir(0, -1); //moves 0 along x and -1 (up) along y axis
    } else if(action == 's') {
        if(snake.yspeed != -1)
            snake.dir(0, 1);
    }
    else if(action == 'd') {
        if(snake.xspeed != -1)
            snake.dir(1, 0);
    }
    else if(action == 'a') {
        if(snake.xspeed != 1)
            snake.dir(-1, 0);
    }
}

function keyPressed() {
    applyAction(key);
}

function getMaps()  {
    // Construct the URL with the message as a query parameter
    var url = 'http://localhost:5001/get_maps';

    // Make a GET request to the server
    fetch(url)
    .then(response => response.json())
    .then(data => {
        // Process the response from the server
        loadMaps(data.maps);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function startMap() {
    empty = [];

    let mapW = Math.floor(w/scl);
    let mapH = Math.floor(h/scl);

    world = new Array(mapW);
    for (let i = 0; i < mapW; i++) {
        world[i] = new Array(mapH);
        for (let j = 0; j < mapH; j++) {
            world[i][j] = '1';
        }
    }     
}

function loadMaps(data)  {
    let select = document.getElementById('maps');

    // Clear select
    select.innerHTML = '';
    select.options.length = 0;
    select.options[select.options.length] = new Option('Novo mapa', '');

    let mapIndex = 1;
    for (var key in data) {
        if (data.hasOwnProperty(key)) {
          let option = document.createElement('option');
          option.value = data[key];
          option.text = key;
          select.appendChild(option);

          mapIndex++;
        }
      }
}

function loadMap(selectedMap) {
    isGameOver = false;
    isLearning = false;
     
    let mapH = selectedMap.split('\n').length - 1; 
    let mapW = selectedMap.split('\n')[0].length;

    empty = [];

    world = new Array(mapW);
    for (let i = 0; i < mapW; i++) {
        world[i] = new Array(mapH);
        for (let j = 0; j < mapH; j++) {
            world[i][j] = selectedMap.split('\n')[j][i];

            if (world[i][j] == 'S') {
                init = createVector(i, j);
                snake = new Snake();
                snake.x = init.x;
                snake.y = init.y;
            }
            else if(world[i][j] == '1') {
                empty.push([i,j]);
            }
            else if(world[i][j] == 'X') {
                walls[[i, j]] = 'X';
            }
        }
    }

    pickLocation(empty);

    // Update scale
    scl = Math.floor(w/mapW) > Math.floor(h/mapH) ? Math.floor(h/mapH) : Math.floor(w/mapW);

    // Enable button
    document.getElementById('startSearch').disabled = false;
}

function worldToMap() {
    let mapW = Math.floor(w/scl);
    let mapH = Math.floor(h/scl);
    
    // Convert world object to string
    let map = '';

    for (let j = 0; j < mapH; j++) {
        for (let i = 0; i < mapW; i++) {
            map += world[i][j];
        }
        map += '\n';
    }

    return map;
}

function draw() {    
    background(255);
    stroke(240);

    for(let i = 0; i < world.length; i++) {
        for(let j = 0; j < world[0].length; j++) {
            if(world[i][j] == 'X') {
                fill(80); 
                rect(i*scl, j*scl, scl, scl);
            }
            else  if(world[i][j] == '1') {
                fill(255);
                rect(i*scl, j*scl, scl, scl);
            }
        }
    }

    //if snake eat food, pick location
    if(snake != null) {
        snake.show();
    }

    if(food != null) {
        //drawing snake food
        fill(255, 0, 100);
        rect(food.x*scl, food.y*scl, scl, scl);
    }
}