import base64
import requests
from pathlib import Path
from github_storage import GitHubStorage

# GitHub konfiguratsiyasi
GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"
GITHUB_TOKEN = "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"
GITHUB_REPO = "YOUR_GITHUB_REPO"


class GitHubStorage:
    """GitHub-ga fayl yuklash va boshqarish uchun yordamchi sinf."""

    GITHUB_API_URL = "https://api.github.com/repos/{username}/{repo}/contents/{file_path}"

    def __init__(self, username=None, repo=None):
        self.username = username or GITHUB_USERNAME
        self.repo = (repo or GITHUB_REPO).replace("https://github.com/", "").replace(".git", "")

        if not self.username or not self.repo:
            raise ValueError("GitHub username yoki repo noto'g'ri sozlangan.")

        self.headers = {
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Content-Type": "application/json",
        }

    def save(self, name, content):
        """Faylni GitHub repozitoriyasiga yuklash yoki yangilash."""
        file_path = f"images/{Path(name).name}"
        encoded_content = base64.b64encode(content).decode("utf-8")

        url = self.GITHUB_API_URL.format(username=self.username, repo=self.repo, file_path=file_path)
        sha = self._get_file_sha(file_path)

        data = {"message": f"Add {name}", "content": encoded_content}
        if sha:
            data["sha"] = sha  # Fayl mavjud bo'lsa, yangilash

        response = requests.put(url, headers=self.headers, json=data)

        if response.status_code in [200, 201]:
            return self.get_file_url(file_path)
        else:
            raise Exception(f"Fayl yuklashda xatolik: {response.status_code} - {response.json()}")

    def _get_file_sha(self, file_path):
        """Faylning SHA qiymatini olish (agar mavjud bo‘lsa)."""
        url = self.GITHUB_API_URL.format(username=self.username, repo=self.repo, file_path=file_path)
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return response.json().get("sha")
        elif response.status_code == 404:
            return None  # Fayl mavjud emas
        else:
            raise Exception(f"SHA olishda xatolik: {response.status_code} - {response.json()}")

    def get_file_url(self, file_path):
        """GitHub-dagi fayl URL manzilini qaytarish."""
        return f"https://raw.githubusercontent.com/{self.username}/{self.repo}/main/{file_path}"


def upload_image(image_url,title):
    response = requests.get(image_url)

    if response.status_code == 200:
        storage = GitHubStorage()  # GitHub bilan bog‘lanish
        image_name = title  # Saqlanadigan fayl nomi
        github_url = storage.save(image_name, response.content)  # GitHub-ga yuklash

        return
        print("Yangi rasm URL:", github_url)  # Olingan rasm URL-sini chiqarish
    else:
        print("Rasmni yuklab bo‘lmadi, status code:", response.status_code)
