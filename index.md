## Welcome to My Pages
<!---
-->
<img src="pic.png" class="img-rounded" width="197" height="281" alt="Something wrong with the picture!"/><br/>
**Pengze Li**<br>
**MSc Computer Graphics, Vision and Imaging**<br>



I am Pengze Li, a college student from University College London(UCL), majoring in Computer Graphics, Vision and Imaging. My research interest focuses on computer vision (e.g., denoising, image processing, recognition), improving image (video) quality and its applications in real-world problems.



**E-mail: LINSONNG@163.COM**<br>
*I sometimes use Sonng Lin as a pseudonym.

### Educations
**Main education experience**<br>
Sep. 2022~Jul. 2023<br>
University College London(UCL)<br>
London,the United Kingdom<br>
Computer Graphics, Vision and Imaging<br>


Sep. 2018~Jul. 2022<br>
Beijing University of Posts and Telecommunications (BUPT)<br>
Beijing, China<br>
B.Eng. in Electronic Science and Technology <br>

Sep. 2015~Jul. 2018<br>
Beijing 101 Middle School <br>
Beijing, China<br>

**Short-term education experience**<br>
Jan. to Feb. 2021(18 contact hours)<br>
School of Continuing and Lifelong Education in collaboration with Faculty of Engineering, National University of Singapore<br>
Online<br>
Programme Name: Artifical Intelligence and Machine Learning<br>

Jul. 2019<br>
STEM summer school, Loughborough University<br>
Leicester, UK<br>
STEM lab

### Research Experience
_Research on Denoising Network Acceleration Based on Convolutional Neural Networks (CNN)_<br>
_Institute of Automation, Chinese Academy of Science_<br>
_Academic Supervisor: Prof. Jian Cheng (Research Fellow), Dr. Chenghua Li, May 2021~June 2022_<br>

In this project, our lab focused on denoising network acceleration based on convolutional neural networks. The research was run with PyTorch, a popular machine learning library, and on GPU (RTX TITAN). Currently, I'm trying to use 3D convolution to further improve my network. Here are some of my work(before 2022.6):<br>
* Reproduced and retrained serveral video-denoising models, all of them were based on or designed from recent papers. <br>
* Tested and reduced the inference time while keeping PSNR(Peak Signal to Noise Ratio) high. <br>
* Pruning was the first way I applied, and I also developed some other architectures and tried many tricks. <br>
* To propose a better motion modeling scheme based on 3D convolution.<br>
* Not only denoising, I also gained some other experience in video super resolution and deploying segmentation networks apps.

_<a target="_blank" href="https://github.com/Linsonng/Linsonng.github.io/blob/main/snowboard1.mp4">Here</a> is a small demonstrate video showing the achievement of the denoising project. Gaussian white noise with a standard deviation of 30 is added to the original video as the upper one. The following video shows the denoising results given by the convolutional neural network in 0.5 seconds. Pause at any time to observe the performance of denoising (loop playing may help)._

<video width="360" height="270" controls>
    <source src="snowboard1.mp4" type="video/mp4">
    Your browser does not support the video tag
</video>

**Multiscale Strip Pooling DLinkNet Enhanced by Channel-wise Attention Mechanism for High Resolution Aerial Image Road Extraction**<br>
_Academic Supervisor: Dr. Junli Yang, Sep 2020~June 2022_<br> 

In the DeepGlobe Road Extraction Challenge, our team aims to receive a better IOU score than other teams. Based on DLinkNet, we managed to improve the score through reproducing and training models on the 3090ti server using PyTorch. We also designed the fusion consisting of multiple models, such as ResNet, D-LinkNet, SENet, D-block, Transformer, and some other new modules. After adopting the pooling feature map to adapt the narrow-and-slender feature in road extraction tasks, we received expected improvements in IoU scores. Moreover, we conducted road extraction tasks based on Transformer and Convolutional Neural Network (CNN), and compared the results of them, which showed that CNN performs better.<br>

Recently, we have completed a paper named Multiscale Strip Pooling DLinkNet Enhanced by Channel-wise Attention Mechanism for High Resolution Aerial Image Road Extraction, which will be soon submitted to Remote Sensing.The research was also run with PyTorch, and on GPU (Tesla V100)<br>

**Research on Pedestrian Classification and Recognition Based on Deep Learning**<br>
_Academic Supervisor: Dr. Da Guo, Prof. Xile Cao.  Jan 2022~June 2022_<br> 
This is my graduation project. In this project, I cooperated with the engineers from Aidong Beyond Artificial Intelligence Technology (Beijing) Co., Ltd.. Based on the private dataset of pedestrians in the factory provided by the company, I completed a pedestrian recognition model based on ResNet, in which I applied data enhancement and other methods. The final recognition rate is greater than 96%. Considering the needs of industry, this project ran with TensorFlow.

Unfortunately, after communicating with the company, I realized that neither the full code files nor the training weights can be made public.

**National University of Singapore Online Winter Programme: Artificial Intelligence and Machine Learning**<br>
_Academic Supervisor: Assoc. Prof. <a target="_blank" href="https://www.linkedin.com/in/motani?originalSubdomain=sg">Mehul Motani</a>, Jan. 2021~Feb. 2021_

This is early and guiding experience in my research.<br>
In the National University of Singapore Online Winter Programme, I studied some supervised learning algorithms, including Linear Regression, Decision Tree, SVM (Support Vector Machine), Neural Networks, and Confusion Matrix, mainly about their concepts and working principles. Besides, I reproduced these models with Python.<br>

Moreover, I leveraged these models and some other extended models to predict the future population of Singapore and China as a completion assignment.<br>

**Research on 5G Frequency Allocation Based on Water Filling Algorithm**<br>
_Academic Supervisor: Prof. <a target="_blank" href="https://www.ee.ucl.ac.uk/~kwong/">Kai-Kit Wong</a> Jul. 2020~Oct. 2020_<br>

When I was focusing on telecommunications, I joined this research in which I studied the communications knowledge of cellular network and frequency planning, including system modeling, channelfading, water-filling power allocation algorithm, and frequency reuse algorithms often used in 4G/ 5G networks, such as IFR(Integer Frequency Reuse) and FFR(Fractional Frequency Reuse). Models were built on Matlab to simulate signal transmission of QPSK, 16-QAM, 64-QAM, etc. Based on the FFR frequency multiplexing algorithm combined with soft frequency reuse (SFR) technique, optimized the frequency allocation algorithm and improved spectral efficiency finallye improved anti-noise performance and channel capacity.<br>

### College Students' Innovative Entrepreneurial Training Plan Programs

The Proper Noun Translator in Thai-and-Chinese Language Based on Python<br>
_Academic Supervisor: Assoc. Prof. Jianming Huang from Jun. 2020 to May. 2021_<br>
* Designed a translator dedicated to translate Thai personal names and geographical names, which mainly contained four modules: Romanization transcription of Thai letters, Roman transcription-Chinese transliteration (corresponded), Dictionary word search and user interface.
* Mainly responsible for realizing the functions mentioned above based on algorithms Python, completed to write the functions, such as cutting the vowels and consonants for Thai and Roman transcriptions, and optimization tasks.
* <a target="_blank" href="https://win.bupt.edu.cn/program.do?id=2559">Intranet link</a>

Develop of an Internet Meme Searching & Compositing Tool Based on Crawling and Artificial <br>
_Academic Supervisor: Prof. Yang Ji from Sep. 2019 to Jul. 2020_<br>
* Crawled copyright-free images from different Internet communities, classified and store them in the database.
* Provided functions of emoji search and use through the WeChat mini program, synthesized pictures and texts, as well as the function of AI face-swap.
* Completed the tasks of image recognition leveraging OpenCV for Python TensorFlow, semantic analysis with TensorFlow for Python, and image crawling using Python, and utilized MySQL in the part of the database.
* Involved in the work of product operation, pre-research, and mid-term project management, and completed some parts of coding tasks.
* <a target="_blank" href="https://win.bupt.edu.cn/program.do?id=1672">Intranet link</a>


College Campus Outdoor-scene Navigation System Based on Unity 3D<br>
_Position: Person in Charge ;Academic Supervisor: Yuan Sun from Jun. 2019 to Jul. 2020_<br>
* This is my first College Students' Innovative Entrepreneurial Training Plan Program, and I am the leader of this Program.
* Using Unity 3D, built a 1: 1 real-scene 3D map of BUPT campus for users to virtually visit the Beijing University of Posts and Telecommunications(My university). Users are able to walk in this map and view the scene.
* Put our 3D map packaged into PC software with some functions released on the mobile phone end and adjusted the adaptability of the mobile end.
* Conducted tasks of project management, algorithm design, and quality test.
* This project scored 90/100 and got selected as the municipal level project in Beijing.
* <a target="_blank" href="https://win.bupt.edu.cn/program.do?id=1179">Intranet link</a>


### HONORS & AWARDS
School-level Scholarship, BUPT	Oct. 2021<br>
Third Prize of the (Microsoft) Imagine Cup Innovation Competition, BUPT Division	Dec. 2020<br>
School-level Scholarship, BUPT	Oct. 2020<br>
School-level Scholarship Learning Progress, BUPT	Oct. 2020<br>
Honorable Mention of China College Students' 'Internet Plus' Innovation and Entrepreneurship Competition	Sep. 2020<br>
Second Prize of the Electronics Information Design Contest, BUPT	May 2020<br>


### Others
Second favourite field: medical science and neuroscience.<br>
Favorite football player: <a target="_blank" href="https://en.wikipedia.org/wiki/Juan_Bernat">Juan Bernat</a><br>
I played right back(No.25) in my college football team.<br>
<img src="Collegeteam.JPG" class="img-rounded" width="600" height="400" alt="Something wrong with the picture!"/><br/>
