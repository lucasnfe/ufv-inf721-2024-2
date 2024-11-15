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
    <th>Lectures</th>
    <th>Readings</th>
    <th>Assignments</th>
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
    <td>
      <a href="https://developers.google.com/machine-learning/intro-to-ml">Google ML, Introduction to Machine Learning</a>
    </td>
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
      <a href="https://youtu.be/nUIU4UUNWVk">[video]</a>
    </td>
    <td>
      <a href="https://developers.google.com/machine-learning/crash-course/linear-regression">Google ML, Linear Regression</a>
    </td>
    <td></td>
  </tr>
  <tr>
    <td>18/09</td>
    <td>4. Logistic Regression<br>
      <a href="{{ 'assets/slides/L04-logistic-regression.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L04-logistic-regression.pdf' | relative_url }}">[notes]</a>
      <a href="{{ 'https://colab.research.google.com/drive/1T9WFg3Du6kRLNcpyVmOMDzsVVHtxm9A_?usp=sharing' | relative_url }}">[code]</a>
      <a href="https://youtu.be/dcDRi5LbbeE">[video 1]</a>
      <a href="https://youtu.be/w8ANvqkW31g">[video 2]</a>
      <a href="https://youtu.be/czXVeuhkjV8">[video 3]</a>
    </td>
    <td>
      <a href="https://developers.google.com/machine-learning/crash-course/logistic-regression">Google ML, Logistic Regression</a>
    </td>
    <td rowspan="3">
      <a href="/assignments/pa1-logistic-regression">PA1: Logistic Regression</a>
    </td>
  </tr>

  <!-- Semana 3 -->
  <tr>
    <td rowspan="2">3</td>
    <td>23/09</td>
    <td>5. MLP<br>
      <a href="{{ 'assets/slides/L05-mlp.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L05-mlp.pdf' | relative_url }}">[notes]</a>
      <a href="https://youtu.be/Egk8lOxanC8">[video]</a></td>
    <td>
      <a href="https://com-cog-book.github.io/com-cog-book/features/multilayer-perceptron.html"> INNMC - The Multilayer Perceptron (Forward propagation)</a>
    </td>
  </tr>

  <tr>
    <td>25/09</td>
    <td>6. Backpropagation<br>
      <a href="{{ 'assets/slides/L06-Backpropagation.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L06-backpropagation.pdf' | relative_url }}">[notes]</a>
      <a href="https://colab.research.google.com/drive/19DfwHu1ZOPGJ8I4fHAzabCgISKc5JEhw?usp=sharing">[code]</a>
      <a href="https://youtu.be/43MVticRn5M">[video]</a>
    </td>
    <td>
      <a href="https://com-cog-book.github.io/com-cog-book/features/multilayer-perceptron.html#Backpropagation-algorithm"> INNMC - The Multilayer Perceptron (Backpropagation)</a>
    </td>
  </tr>

  <!-- Semana 5 -->
  <tr>
    <td rowspan="2">4</td>
    <td>30/09</td>
    <td><b>Holiday (Dia da Cidade)</b></td>
    <td></td>
    <td rowspan="3"><a href="/assignments/pa2-multilayer-perceptron">PA2: Multilayer Perceptron</a></td>
  </tr>
  <tr>
    <td>02/10</td>
    <td>7. Evaluting Neural Networks<br>
      <a href="{{ 'assets/slides/L07-evaluating-models.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L07-evaluating-models.pdf' | relative_url }}">[notes]</a>
      <a href="https://colab.research.google.com/drive/1Upq6ugok09FHRi3SzCpDdbPCEDr3uGTF?usp=sharing">[code]</a>
      <a href="https://youtu.be/5uAzT4FxzbE">[video]</a>
    </td>
    <td>
    <a href="https://developers.google.com/machine-learning/crash-course/classification">Google ML, Classification</a>
    </td>
  </tr>

  <!-- Semana 6 -->
  <tr>
    <td rowspan="2">5</td>
    <td>07/10</td>
    <td>8. Regularization<br>
      <a href="{{ 'assets/slides/L08-regularization.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L08-regularization.pdf' | relative_url }}">[notes]</a>
      <a href="{{ '#' | relative_url }}">[code]</a>
      <a href="https://youtu.be/8PH78PJ-WxA">[video]</a>
    </td>
    <td>
      <a href="https://issuu.com/cmb321/docs/deep_learning_ebook/270">Bishop 2024, Ch. 9: Regularization</a>
    </td>
  </tr>
  <tr>
    <td>09/10</td>
    <td>9. Advanced Optimization Algorithms<br>
      <a href="{{ 'assets/slides/L09-optimization.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L09-optimization.pdf' | relative_url }}">[notes]</a>
      <a href="https://colab.research.google.com/drive/10SfBw31B0zA3yd5wFzjz9P5gy8x_R_dG?usp=sharing">[code]</a>
      <a href="https://youtu.be/5k47BbWpUsM">[video]</a>
    </td>
    <td>
      <a href="https://issuu.com/cmb321/docs/deep_learning_ebook/226">Bishop 2024, Ch. 7: Gradient Descent</a>
    </td>
    <td></td>
  </tr>

  <!-- Semana 7 -->
  <tr>
    <td rowspan="2">6</td>
    <td>14/10</td>
    <td><b>Midterm Exam I</b></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>16/10</td>
    <td>10. CNNs I<br>
      <a href="{{ 'assets/slides/L10-cnn1.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L10-cnn1.pdf' | relative_url }}">[notes]</a>
      <a href="https://setosa.io/ev/image-kernels/">[demo]</a>
      <a href="https://youtu.be/HOYlW_F36mY">[video]</a>
    </td>
    <td>
    <a href="https://issuu.com/cmb321/docs/deep_learning_ebook/302">Bishop 2024, Ch. 10: Convolutional Networks (287-296)</a>
    </td>
    <td rowspan="3"><a href="/assignments/pa3-cnn">PA3: Convolutional Neural Networks</a></td>
  </tr>

  <!-- Semana 8 -->
  <tr>
    <td rowspan="2">7</td>
    <td>21/10</td>
    <td>11. CNNs II<br>
    </td>
      <a href="{{ 'assets/slides/L11-cnn2.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L11-cnn2.pdf' | relative_url }}">[notes]</a>
      <a href="https://youtu.be/pCTIaz-6ieg">[video]</a>
    <td>
        <a href="https://issuu.com/cmb321/docs/deep_learning_ebook/312">Bishop 2024, Ch. 10: Convolutional Networks (296-301)</a>
    </td>
  </tr>
  <tr>
    <td>23/10</td>
    <td>12. Normalization<br>
      <a href="{{ 'assets/slides/L12-normalization.pdf' | relative_url }}">[slides]</a>
      <a href="{{ 'assets/notes/L12-normalization.pdf' | relative_url }}">[notes]</a>
      <a href="https://colab.research.google.com/drive/1ENxS8fY82k12ePPsNFkzHEEhoetpH7Tm?usp=sharing">[code]</a>
      <a href="https://youtu.be/LcjdhyLVJKQ">[video]</a>
    </td>
    <td>
      <a href="https://issuu.com/cmb321/docs/deep_learning_ebook/312">Bishop 2024, Ch. 7: Gradient Descent (226-230)</a>
    </td>
    <!-- <td></td> -->
  </tr>  

  <!-- Semana 9 -->
  <tr>
    <td rowspan="2">8</td>
    <td>28/10</td>
    <td>13. RNNs I<br>
      <a href="{{ 'assets/slides/L13-rnn1.pdf' | relative_url }}">[slides]</a>
      <a href="https://youtu.be/tHTns0ag710">[video]</a>
    </td>
    <td>
        <a href="https://com-cog-book.github.io/com-cog-book/features/recurrent-net.html"> INNMC - The Recurrent Neural Network (Elman Network)</a>
    </td>
    <td rowspan="3"><a href="/assignments/pa4-rnn">PA4: Recurrent Neural Networks</a></td>
  </tr>
  <tr>
    <td>30/10</td>
    <td>14. RNNs II<br>
      <a href="{{ 'assets/slides/L14-rnn2.pdf' | relative_url }}">[slides]</a>
      <a href="https://youtu.be/Aetd41ovh-c">[video]</a>
    </td>
    <td>
            <a href="https://com-cog-book.github.io/com-cog-book/features/recurrent-net.html#Long-Short-Term-Memory-Network"> INNMC - The Recurrent Neural Network (LSTM)</a>
    </td> 
    <!-- <td></td> -->
  </tr>  

  <!-- Semana 10 -->
  <tr>
    <td rowspan="2">9</td>
    <td>04/11</td>
    <td>15. Word Embeddings<br>
      <a href="{{ 'assets/slides/L15-word-embedding.pdf' | relative_url }}">[slides]</a>
      <a href="https://youtu.be/K5HXZoM0Ci0">[video]</a>
    </td>
    <td></td>
    <!-- <td></td> -->
  </tr>
  <tr>
    <td>06/11</td>
    <td>16. Attention<br>
      <a href="{{ 'assets/slides/L16-attention.pdf' | relative_url }}">[slides]</a>
      <a href="https://colab.research.google.com/drive/15H47hgj892aD_PGgRJ1mpkhAzfuRQ_cj?usp=sharing">[code]</a>
    </td>
    <td></td>
    <td rowspan="9">FP2: Project Implementation</td>
  </tr>  

  <!-- Semana 11 -->
  <tr>
    <td rowspan="2">10</td>
    <td>11/11</td>
    <td>17. Transformers I<br>
      <a href="{{ 'assets/slides/L17-transformers1.pdf' | relative_url }}">[slides]</a>
    </td>
    <td>
    <a href="https://nlp.seas.harvard.edu/annotated-transformer"> The Annotated Transformer - The Harvard NLP Group</a>
    </td>
  </tr>
  <tr>
    <td>13/11</td>
    <td>18. Transformers II<br>
      <a href="{{ 'assets/slides/L18-transformers2.pdf' | relative_url }}">[slides]</a>
      <a href="https://colab.research.google.com/drive/1fjX6u-05vl-YCxSzlGKkhhh31asw4Eg-?usp=sharing">[code]</a>
    </td>
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
