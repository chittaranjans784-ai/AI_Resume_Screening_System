from django.db import models


# ==========================================================
# Register Model
# ==========================================================

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

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.fullname


# ==========================================================
# Resume Model
# ==========================================================

class Resume(models.Model):
    user = models.ForeignKey(
        Register,
        on_delete=models.CASCADE,
        related_name="resumes"
    )

    resume = models.FileField(upload_to="resume/")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    extracted_text = models.TextField(
        blank=True,
        null=True
    )

    ats_score = models.IntegerField(default=0)

    skills_found = models.TextField(
        blank=True,
        null=True
    )

    missing_skills = models.TextField(
        blank=True,
        null=True
    )

    ai_suggestion = models.TextField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ["-uploaded_at"]
        verbose_name = "Resume"
        verbose_name_plural = "Resumes"

    def __str__(self):
        return f"{self.user.fullname} - {self.uploaded_at.strftime('%d-%m-%Y %H:%M')}"


# ==========================================================
# Contact Model
# ==========================================================

class Contact(models.Model):
    user = models.ForeignKey(
        Register,
        on_delete=models.CASCADE,
        related_name="contacts"
    )

    name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(max_length=200)

    message = models.TextField()

    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return self.subject