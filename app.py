from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    profile = {
        "name": "Tuğba Aktaş",
        "title": "Bilgisayar Mühendisi",
        "linkedin": "tugbaaktas",
        "github": "tubaaktas",
        "medium": "kendine_muhendis",
        "email": "tubaaktas83@gmail.com",
        "phone": "+90 545 945 31 91",
        "address": "Derince, Kocaeli, Türkiye",
        "about": (
            "Bilgisayar mühendisliği mezunuyum. Yazılım, donanım, veri bilimi ve DevOps "
            "teknolojilerinde bilgi ve becerilerimi geliştirmek için projeler üretmeyi seviyorum. "
            "AWS servisleri, Kubernetes, Terraform ve veri bilimi araçlarıyla çalıştım. Takım çalışmasına yatkın, "
            "teknolojinin her alanında öğrenmeye açık ve dinamik bir yapıya sahibim."
        )
    }

    experience = [
        {
            "title": "IEEE Computer Society Üyesi",
            "company": "Tekirdağ Namık Kemal Üniversitesi",
            "date": "Eylül 2019 - Eylül 2021"
        },
        {
            "title": "Teknik Servis Çalışanı",
            "company": "Özgür Bilgisayar",
            "date": "Eylül 2020 - Nisan 2021"
        },
        {
            "title": "Data Scientist Mentor Yardımcısı",
            "company": "Miuul",
            "date": "Eylül 2023 - Devam Ediyor"
        },
        {
            "title": "DevOps Intern",
            "company": "Artifact System",
            "date": "29 Temmuz 2024 - Devam Ediyor",
            "description": (
                "2 Ay zorunlu stajımın yanında gönüllü olarak stajıma devam ettiğim Artifact'de"
                "AWS servisleri, Kubernetes, Helm, Terragrunt, DigitalOcean, GitHub ve GitLab gibi "
                "teknolojilerle çalışma deneyimi kazandım."
            )
        }
    ]

    education = [
        {
            "degree": "Bilgisayar Mühendisliği",
            "school": "Tekirdağ Namık Kemal Üniversitesi",
            "date": "Eylül 2018 - 2024",
            "gpa": 3.19
        },
        {
            "degree": "Yazılım Öğrencisi",
            "school": "Ecole42 Kocaeli / Bilişim Vadisi",
            "date": "Eylül 2021 - Haziran 2022"
        },
        {
            "degree": "Yazılım Geliştirici Yetiştirme Kampı",
            "school": "Kodlama.io",
            "date": "Şubat 2021"
        },
        {
            "degree": "Veri Bilimi Öğrencisi",
            "school": "Miuul Makine Öğrenimi Yaz Kampı",
            "date": "Temmuz 2022 - Ağustos 2022"
        },
        {
            "degree": "Veri Bilimi Öğrencisi",
            "school": "Miuul Data Science Bootcamp 12. Dönem",
            "date": "Haziran 2023 - Eylül 2023"
        },
        {
            "degree": "AWS Öğrencisi",
            "school": "Miuul AWS Cloud Technical Bootcamp",
            "date": "Haziran 2023"
        }
    ]

    skills = [
        "Python", "AWS", "Kubernetes", "Helm", "Terragrunt","Elasticsearch",
        "DigitalOcean", "GitHub", "GitLab", "Makine Öğrenimi", "Veri Bilimi", "CRM"
    ]

    return render_template("index.html", profile=profile, experience=experience, education=education, skills=skills)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
