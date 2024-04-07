# Project Title

Django LMS allows you to curate courses for your students and track learning progress in real time.

## Table of Contents

- [Project Title](#project-title)
- [Description](#description)
- [Installation](#installation)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Description

In this new digital era, physical meet point such as classrooms are diminishing in purpose. Learners want comfortability while learning and also want a better experience. With this learning management system, educators can now create courses for students, associate relevant modules to those courses, have students enrol and track the learning progress. While the system has simple functionalities (in code), it also has a deeper meaning in real life use cases. 

## Installation

Setting up and installing this project is quite straightforward and easy. Below are detailed step on how to get this web app up and running. 

1. Install a virtual environment. (Skip if you already have this installed) 
```bash
pip intall virtualenv

```

2. Create and activate a virtual environment 
```bash
virtualenv generic_name

cd generic_name && Scripts\activate
```

3. Clone the project's github repo and cd into project
```bash
git clone https://github.com/chideegit/lms.git

cd django-lms
```

4. Install all the dependencies contained in the [requirements.txt](./requirements.txt) file. 
```bash
pip install -r requirements.txt
```

5. Make migrations, migrate and  then run local server 
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Contributing
If you would like to contribute to the project, please follow the guidelines outlined in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

## License
This project is licensed under the MIT License - see the [LICENSE file](./LICENSE) for details.

## Acknowledgments
Special thanks to the Django community for providing a robust framework.

Feel free to reach out for any questions, issues, or feature requests!

Happy coding🚀