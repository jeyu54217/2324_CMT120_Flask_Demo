# c23021947_cmt120_cw2

## About This Project
This project is a dynamic digital portfolio website, showcasing my education and experience. It's built with Python Flask and Jinja2 for backend and content rendering, and incorporates SQLAlchemy as the ORM system. The site uses Bootstrap for responsive design and is deployed on Red Hat OpenShift. This forms part of my CMT120 coursework.

- [Demo Website](https://cmt120-flask-cardiff-2324-cmt120-flask-c23021947.apps.containers.cs.cf.ac.uk/)  (on OpenShift): (Activate the [Cardiff University VPN](https://intranet.cardiff.ac.uk/students/it-support/wireless-and-remote-access/remote-access/vpn-virtual-private-network) to access.)

## Main Features
- User authentication system for login functionality.
- Implementation of cascading deletions, where removing user automatically deletes all
its linked data.
- Design of a low-coupling test data script for more efficient testing.
- Redirecting users without proper authorization away from restricted pages
- Dynamic navigation bar that alters its appearance based on user login status.
- Use of Bootstrap for a responsive and adaptable site layout.
- Display of flash messages during editing, Login, and Logout for better user
interaction.

## Setting Up
- venv
    ```bash
    python3 -m venv venv
    ```
    ```bash
    source venv/bin/activate
    ```
- Install Packages
    ```bash
    pip install -r requirements.txt
    ```
- Generate Test Data for DB
    ```bash
    python3 <path/to>/db_creation.py
    ```
- Run Flask Locally
    ```bash
    flask run
    ```
## Screenshot
### Home Page
<img width="1649" alt="Screenshot 2024-01-12 at 08 40 20" src="https://github.com/jeyu54217/2324_CMT120_Flask_Demo/assets/73396926/8456e8d5-654c-4461-8df3-2e2742ebcf77">

### Login
<img width="1685" alt="Screenshot 2024-01-12 at 08 40 57" src="https://github.com/jeyu54217/2324_CMT120_Flask_Demo/assets/73396926/24111655-71d1-404e-a0eb-3f3c84336610">

### Edit Content
<img width="1685" alt="Screenshot 2024-01-12 at 08 41 29" src="https://github.com/jeyu54217/2324_CMT120_Flask_Demo/assets/73396926/bd6dbc11-92ee-4976-8686-e193ebbccc62">

