# Enhanced Iris Recognition with Data Augmentation
## Environment:
---
- Python 3.11.6
- Library : 
  - numpy==1.26.4
  - pandas==2.2.2
  - PySimpleGUI==5.0.4
  - tensorflow==2.16.1

## How to use ?
### Demo
---
The following command runs the python´s demo. Moving the slide bar will automatically generate a new iris image with the selected dilation level and display it. To switch images, first select the desired image with the scroll element on top and then press the Apply button.

```bash
python Demo.py
```

### Generate Images
---
The following command will diversify a data layer by generating objects with different iris elasticity, increasing the recognition ability of machine learning and deep learning models. They are saved to the train2 folder in the Dataset folder.

```bash
python generate_images.py
```

### Apply model
---
The model we use here will be the ResNet50 deep learning model. To run the notebook file below, you must follow these steps:
1. Open google colab and add the notebook file.
2. Create a data folder on the drive to match the path set in the notebook file.
3. Select the training data to see their differences by changing the path name to the folder containing the training data.
  
    3.1. We have 2 sets of training data: `Train1` and `Train2`. Where `Train1` is data that has not been augmented and `Train2` is data that has been augmented.
  
    3.2. To make it easier, we will find the variable named `train_data_dir` and change the path to the training data we want.
    
4. Now we can run all the cells to see the results.
