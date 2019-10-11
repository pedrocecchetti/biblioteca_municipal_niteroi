from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, cpf, password=None):
            """
            Creates a new user with the given Email and Password
            """
            if not email:
                raise ValueError("Users must have email address")

            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save(using=self._db)

            return user
    
    def create_superuser(self, email, first_name, last_name, cpf, password=None):
        """
        Creates a SUPERUSER with email and password given
        """ 

        user = self.create_user(email, first_name, last_name, cpf, password=password)
        user.first_name = first_name
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    # Identity
    first_name = models.CharField(max_length=20, verbose_name='Nome')
    last_name = models.CharField(max_length=150, verbose_name='Sobrenome')
    cpf = models.CharField(max_length=11, verbose_name='CPF',help_text='Somente Números')

    # Authentication
    email = models.EmailField(unique=True, verbose_name='E-mail')
    password = models.CharField(max_length=128, verbose_name='Password')

    # Status and Permissions
    is_active = models.BooleanField(default=True, verbose_name='Usuário Ativo?')
    is_staff = models.BooleanField(default=False, verbose_name='Usuário com acesso ao Admin?')
    is_superuser = models.BooleanField(default=False, verbose_name='Acesso de SuperUsuário?')

    # Monitoring
    last_login = models.DateTimeField(null=True, verbose_name='Último Login')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Última edição')

    # Associations
    groups = models.ManyToManyField(
        blank=True,
        help_text='Grupo de permissão do usuário.',
        related_name='user_groups',
        related_query_name='user',
        to='auth.Group',
        verbose_name='Grupos de Usuário',
    )
    
    permissions = models.ManyToManyField(
        blank=True,
        help_text='Permissões do usuário.',
        related_name='user_permissions',
        related_query_name='user',
        to='auth.Permission',
        verbose_name='Permissões do Usuário',
    )

    object = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cpf']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return '{} - {}'.format(self.first_name, self.email)