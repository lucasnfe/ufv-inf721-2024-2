---
layout: page
title: Schedule
description: Listing of course modules and topics.
---

# Schedule

Course schedule following the [[CEPE RESOLUTION Nº 7/2024]](https://www2.dti.ufv.br/noticias/files/anexos/1719953979.pdf):

<!-- {% for module in site.modules %}
{{ module }}
{% endfor %} -->

<table>
  <tr>
    <th>Week</th>
    <th>Date</th>
    <th>Lecture</th>
    <th>Reading</th>
    <th>Assignment</th>
  </tr>

  <!-- Semana 1 -->
  <tr>
    <td rowspan="2">1</td>
    <td>09/09</td>
    <td>1. Introduction<br><a href="{{ 'assets/slides/L01-introduction.pdf' | relative_url }}">[slides]</a><a href="https://youtu.be/77FNyBwjdV8">[video]</a></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>11/09</td>
    <td>2. Machine Learning<br><a href="{{ 'assets/slides/L02-machine-learning.pdf' | relative_url }}">[slides]</a><a href="{{ 'assets/notes/L02-machine-learning.pdf' | relative_url }}">[notes]</a><a href="https://youtu.be/8iulB8B1iKE">[video]</a></td>
    <td><a href="https://d2l.ai/chapter_introduction/index.html">Dive Into Deep Learning, Ch. 1. Introduction</a></td>
    <td></td>
  </tr>

  <!-- Semana 2 -->
  <tr>
    <td rowspan="2">2</td>
    <td>16/09</td>
    <td>3. Linear Regression<br>
      <a href="{{ 'assets/slides/L03-linear-regression.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L03-linear-regression.pdf' | relative_url }}">[notes]</a>
      <a href="https://colab.research.google.com/drive/1wBSS1M9A3BqGwxSjmsSpLtGGwDCD5Ayh?usp=sharing">[code]</a>
      <a href="https://youtu.be/nUIU4UUNWVk">[video]</a></td>
    <td></td>
    <td rowspan="3">PA1: Logistic Regression</td>
  </tr>
  <tr>
    <td>18/09</td>
    <td>4. Logistic Regression<br>
      <a href="{{ 'assets/slides/L04-logistic-regression.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L04-logistic-regression.pdf' | relative_url }}">[notes]</a>
      <a href="{{ 'https://colab.research.google.com/drive/1T9WFg3Du6kRLNcpyVmOMDzsVVHtxm9A_?usp=sharing' | relative_url }}">[code]</a>
      <a href="https://youtu.be/dcDRi5LbbeE">[video 1]</a>
      <a href="https://youtu.be/w8ANvqkW31g">[video 2]</a>
      <a href="https://youtu.be/czXVeuhkjV8">[video 3]</a></td>
    <td></td>
  </tr>

  <!-- Semana 3 -->
  <tr>
    <td rowspan="2">3</td>
    <td>23/09</td>
    <td>5. MLP I<br>
      <a href="{{ 'assets/slides/L05-MLP1.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L5-MLP1.pdf' | relative_url }}">[notes]</a>
      <a href="https://youtu.be/Egk8lOxanC8">[video]</a></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>25/09</td>
    <td>7. MLP II</td>
    <td></td>
    <td rowspan="3">PA2: Multilayer Perceptron</td>
  </tr>

  <!-- Semana 5 -->
  <tr>
    <td rowspan="2">4</td>
    <td>30/09</td>
    <td>8. Evaluting Neural Networks</td>
    <td></td>
  </tr>
  <tr>
    <td>02/10</td>
    <td>9. Advanced Optimization Algorithms</td>
    <td></td>
  </tr>

  <!-- Semana 6 -->
  <tr>
    <td rowspan="2">5</td>
    <td>07/10</td>
    <td>10. Regularization & Normalization</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>09/10</td>
    <td><b>Midterm Exam I</b></td>
    <td></td>
    <td></td>
  </tr>

  <!-- Semana 7 -->
  <tr>
    <td rowspan="2">6</td>
    <td>14/10</td>
    <td>11. CNNs I</td>
    <td></td>
    <td rowspan="3">PA3: Convolutional Neural Networks</td>
  </tr>
  <tr>
    <td>16/10</td>
    <td>12. CNNs II</td>
    <td></td>
  </tr>

  <!-- Semana 8 -->
  <tr>
    <td rowspan="2">7</td>
    <td>21/10</td>
    <td>13. RNNs I</td>
    <td></td>
  </tr>
  <tr>
    <td>23/10</td>
    <td>14. RNNs II</td>
    <td></td>
    <td rowspan="3">PA4: Recurrent Neural Networks</td>
  </tr>  

  <!-- Semana 9 -->
  <tr>
    <td rowspan="2">8</td>
    <td>28/10</td>
    <td>15. Word Embeddings</td>
    <td></td>
  </tr>
  <tr>
    <td>30/10</td>
    <td><b>Feriado Municipal (Dia da Cidade)</b></td>
    <td></td> 
  </tr>  

  <!-- Semana 10 -->
  <tr>
    <td rowspan="2">9</td>
    <td>04/11</td>
    <td>15. Attention</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>06/11</td>
    <td>16. Transformers I</td>
    <td></td>
    <td rowspan="9">FP2: Project Implementation</td>
  </tr>  

  <!-- Semana 11 -->
  <tr>
    <td rowspan="2">10</td>
    <td>11/11</td>
    <td>17. Transformers II</td>
    <td></td>
  </tr>
  <tr>
    <td>13/11</td>
    <td>18. Transfer Learning</td>
    <td></td>
  </tr>  

  <!-- Semana 12 -->
  <tr>
    <td rowspan="2">11</td>
    <td>18/11</td>
    <td><b>Midterm Exam II</b></td>
    <td></td>
  </tr>
  <tr>
    <td>20/11</td>
    <td>19. Transfer Learning</td>
    <td></td>
  </tr>  

  <!-- Semana 13 -->
  <tr>
    <td rowspan="2">12</td>
    <td>25/11</td>
    <td>20. GANs</td>
    <td></td>
  </tr>
  <tr>
    <td>27/11</td>
    <td>21. Variational Autoencoders</td>
    <td></td>
  </tr>  

  <!-- Semana 14 -->
  <tr>
    <td rowspan="2">13</td>
    <td>02/12</td>
    <td>22. Diffusion Models</td>
    <td></td>
  </tr>
  <tr>
    <td>04/12</td>
    <td>23. Multimodal Learning</td>
    <td></td>
  </tr>  

  <!-- Semana 15 -->
  <tr>
    <td rowspan="2">14</td>
    <td>09/12</td>
    <td>24. Final Project Presentation I</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>11/12</td>
    <td>24. Final Project Presentation II</td>
    <td></td>
    <td></td>
  </tr>  

</table>
