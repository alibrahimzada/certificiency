import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';
import { authErrors } from './../../core/errors';
import { AlertService } from './../../core/services/alert.service';
import { LoadingService } from './../../core/services/loading.service';
import { RoleService } from './../../core/services/role.service';
declare const $: any;
@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  credentials = {
    username: '',
    password: ''
  };
  resetPassword = {
    email: '',
    code: '',
    password: '',
    passwordAgain: '',
    step: 0
  }
  constructor(
    private authService: AuthService,
    private router: Router,
    private alertService: AlertService,
    private loadingService: LoadingService,
    private roleService: RoleService,
  ) { }

  ngOnInit(): void {
    const token = this.authService.getToken();
    if (token) {
      this.router.navigate(['/']);
    }
    this.authService.helloWorld().subscribe(response =>{
      console.log(response);
    })
  }

  login() {
    this.loadingService.setLoading(true);
    this.authService.login(this.credentials).subscribe(response => {
      console.log(response);
      const { success, errors } = response;
      if (success === true) {
        this.authService.saveUserToLocalStorage(response);
        this.roleService.getCurrentUserRoles().subscribe(response => {
          this.router.navigate(['/']);
        })
      } else {
        this.alertService.alert('Hata!', authErrors.login[errors[0]], 'error');
      }
      this.loadingService.setLoading(false);
    })
  }

  showPasswordModal() {
    this.resetPassword = {
      email: '',
      code: '',
      password: '',
      passwordAgain: '',
      step: 0
    }
    $('.modal').modal('show');
  }
  hidePasswordModal() {
    this.resetPassword = {
      email: '',
      code: '',
      password: '',
      passwordAgain: '',
      step: 0
    }
    $('.modal').modal('hide');
  }

  sendCode() {
    this.authService.sendCode(this.resetPassword.email).subscribe(response => {
      if (response.success) {
        this.alertService.alert('Başarılı!', 'Kod mail adresinize başarıyla gönderildi.', 'success');
        this.resetPassword.step = 1;
      } else {
        this.alertService.alert('Hata!', 'Kullanıcı bulunamadı.', 'error');
      }
    });
  }
  changePassword() {
    this.authService.changePassword(this.resetPassword.email, this.resetPassword.code, this.resetPassword.passwordAgain).subscribe(response => {
      if (response.success) {
        this.alertService.alert('Başarılı!', 'Şifreniz başarıyla değiştirildi.', 'success');
        this.hidePasswordModal();
      } else {
        this.alertService.alert('Hata!', 'Kodu kontrol ediniz..', 'error');
      }
    });
  }
}
