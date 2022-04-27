폐질환 의심 응급환자의 진단과정 단축을 위한 AI 흉부 X-ray 진단 보조 서비스
=============

## 주제 구체화 과정
#### `1) 의료 환경 리서치`
세계적인 펜데믹으로 인해 응급환자의 수는 계속해서 증가하고 있다. 여러분도 응금실을 방문했을 때 대기시간이 길어 어려움을 느낀 적이 있을 것이다. 특히 응급실을 찾는 환자의 절반 이상(56%)이 엑스레이 촬영을 받고 있다. 그 중 흉부외과는 x-ray 촬영률이 90%로 가장 높았다. 흉부손상은 외상으로 인한 사망의 20~25%를 차지할 정도로 적정시기의 적절한 치료가 매우 중요하다. 하지만 x-ray 진단에 소요되는 시간은 3371초, 약 1시간으로 골든타임이 중요한 응급환자에게는 긴 시간일 것이다. 응급실에서의 대기시간에 대한 만족도 조사에 의하면 40점대로 낮다는 것도 확인할 수 있었다. 

#### `2) 의료 환경 문제점 분석`
이렇게 진단 시간이 많이 걸리는 이유는 다음과 같이 네단계의 프로세스로 진행되기 때문이었다. x-ray 촬영을 한 후 그 결과를 바탕으로 추가 검사 여부를 결정하게 되며 이 후 ct나 mri 등의 추가 검사를 마친 후에 최종진단에 이르게 된다. 각 프로세스별 대기시간까지 고려한다면 분명 적지 않은 시간일 것이다. 그래서 저희는 추가 검사를 생략한, x-ray 촬영만으로 최종진단에 이르는 단축된 진단 프로세스를 생각해 보게 되었다.

#### `3) 기대되는 점`
진단 속도 12초로 응급환자의 x-ray 이미지를 진단할 수 있는 정확도 97.1, auc 84.12의 서비스를 제작했다. 다음은 실제 서비스의 시연 캡처화면이며 x-ray 이미지를 업로드하면 상위 3개의 질병을 확률값과 함께 보여준다. 빨간 박스는 질병으로 의심되는 영역을 표시해 준다.



이를 구현하기 위해 Classification and Detection 기반 Web Service를 구현했으며, Classification 성능을 향상시키기 위해 PGGAN을 사용하여 합성 의료 X선 데이터를 생성했다. 문제가 있는 부위 특정, X선 처리시간 단축, 응급환자의 정확한 질병분류 등 의료과정의 효율성 향상에 활용될 것으로 기대된다.

<img src="https://user-images.githubusercontent.com/71118045/144365814-59484285-4c11-48ce-8e2a-cd99ccc134ad.PNG" width="600" height="300"/>

It is an explanation of the system structure of the program. Starting from the right, uploading the x-ray image from the website requests classification and detection diagnosis of the image at the backend. Then, the uploaded image is classified with the learned model. In the case of Detection, learning is conducted using the yolov5 model. Then, the suspected disease area is detected with the uploaded image and the resulting image is stored. Through this process, a screen is finally output as a result of diagnosing the patient's disease on the website screen and detecting the suspected disease occurrence site. Three possible diseases are presented to help doctors diagnose diseases quickly.

<img src="https://user-images.githubusercontent.com/71118045/144364448-1fdd71ac-c470-46ed-8b56-d014affe6594.PNG" width="500" height="300"/>

## :sparkles:0. Dataset

Chest X-ray exams are one of the most frequent and cost-effective medical imaging examinations available. However, clinical diagnosis of a chest X-ray can be challenging and sometimes more difficult than diagnosis via chest CT imaging. The lack of large publicly available datasets with annotations means it is still very difficult, if not impossible, to achieve clinically relevant computer-aided detection and diagnosis (CAD) in real world medical sites with chest X-rays. One major hurdle in creating large X-ray image datasets is the lack resources for labeling so many images. Prior to the release of this dataset, Openi was the largest publicly available source of chest X-ray images with 4,143 images available.

This NIH Chest X-ray Dataset is comprised of 112,120 X-ray images with disease labels from 30,805 unique patients. To create these labels, the authors used Natural Language Processing to text-mine disease classifications from the associated radiological reports. The labels are expected to be >90% accurate and suitable for weakly-supervised learning. The original radiology reports are not publicly available but you can find more details on the labeling process in this Open Access paper: "ChestX-ray8: Hospital-scale Chest X-ray Database and Benchmarks on Weakly-Supervised Classification and Localization of Common Thorax Diseases." (Wang et al.)

###### https://www.kaggle.com/nih-chest-xrays/data

## :sparkles:1. Classification

<img src="https://user-images.githubusercontent.com/71118045/144366234-16d81ff2-3980-4499-96c6-4c4218b2dd28.PNG"  width="900" height="300"/>

###### Weights: [Google Drive Link](https://drive.google.com/drive/folders/1-uo9GchtOoAFvXmE0zpPi0eaFgKNOrk6?usp=sharing)

## :sparkles:2. Detection

###### Training Data: [Google Drive Link](https://drive.google.com/drive/folders/11CUJGctnzHQcsq9O3WCSTRhgRjkMOOUN?usp=sharing)
###### Ultralytics Yolov5 : https://github.com/ultralytics/yolov5

<img src="./Result_Image/Detection_NIH_200.jpg"  width="400" height="400"/>

###### Result of NIH Data: [Google Drive Link](https://drive.google.com/drive/folders/1qo_5ICzeMUrHQ_-s0Z9d3KYSLCrNzqRl?usp=sharing)
###### Result of ChestX Data : [Google Drive Link](https://drive.google.com/drive/folders/1NBvWFz3Fto6ZqeLrqopEMlbUZnNpxodN?usp=sharing)
###### Result of NIH & ChestX Data: [Google Frive Link](https://drive.google.com/drive/folders/1Koryg3pxeUs7oJ0ulO7FEjrq0EMPB6of?usp=sharing)

## :sparkles:3. GAN Research

<img src="https://user-images.githubusercontent.com/85219925/144364517-22de0573-d468-433f-95d4-b4eaac10f902.png"  width="400" height="400"/>

###### Generated Image(PGGAN1): [Google Drive Link](https://drive.google.com/drive/folders/1qJj4dn9ap-fPbrHuP2OR9f7_tTKUm58L?usp=sharing)
###### Generated Image(PGGAN2): [Google Drive Link](https://drive.google.com/drive/folders/1IWavLvJQTNJ_Ui-s0R7is2MTI1Q3naOe?usp=sharing)
###### Generated Image(PGGAN3): [Google Drive Link](https://drive.google.com/drive/folders/1q1PmqqxZPPGEzazGkzOXv4WF1G5zFNO1?usp=sharing)
###### PGGAN Weights: [Google Drive Link](https://drive.google.com/drive/folders/1Y9l7wqjt-cKR-gJRIe8DqZwbG91nyXEy?usp=sharing)

###### Generated Image(DCGAN): [Google Drive Link](https://drive.google.com/drive/folders/18MekMJsuhZS6Shu3T6nvmNihK4M4oilz?usp=sharing)

## :book:Papers
###### 1. 폐질환 의심 응급환자의 진단 과정 단축을 위한 AI기반 X-ray진단 시스템
###### https://drive.google.com/file/d/1FnQGBRWvJ70iH2Rut0L7hjO-4Bt15vpc/view?usp=sharing
###### 2. PGGAN synthetic data를 활용한 Class간 데이터분포의 불균형 완화가 X-ray 질병 진단 정확도에 미치는 영향 연구
###### https://drive.google.com/file/d/1OPLWdxKm7L0jW0QhTIYEo4-7AER3-JNz/view?usp=sharing

## :REFERENCE
###### https://www.koreascience.or.kr/article/JAKO201123736032447.pdf
