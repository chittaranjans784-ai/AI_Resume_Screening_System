from django.db import models

class Register(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_photo = models.ImageField(
        upload_to="profile/",
        default="profile/default.png",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.fullname
    
    


class Resume(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="resume/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    extracted_text = models.TextField(blank=True, null=True)

    ats_score = models.IntegerField(default=0)

    skills_found = models.TextField(blank=True, null=True)

    missing_skills = models.TextField(blank=True, null=True)

    ai_suggestion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.fullname
    

# ==========================================================
# Contact Model
# ==========================================================

class Contact(models.Model):

    user = models.ForeignKey(
        Register,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject