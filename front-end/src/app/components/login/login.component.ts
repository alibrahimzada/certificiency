import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';
import { UserService } from 'src/app/core/services/user.service';
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
    private userService: UserService,
    private loadingService: LoadingService,
    private roleService: RoleService,
  ) { }

  ngOnInit(): void {
    const token = this.authService.getToken();
    if (token) {
      this.router.navigate(['/']);
    }
  }

  login() {
    this.loadingService.setLoading(true);
    this.authService.login(this.credentials).subscribe(response => {
      console.log(response);
      const { success, errors } = response;
      if (success === true) {
        this.authService.saveUserToLocalStorage(response);
        // this.roleService.getCurrentUserRoles().subscribe(response => {
        //   this.router.navigate(['/']);
        // })
        this.router.navigate(['/']);
      } else {
        this.alertService.alert('Error!', authErrors.login[errors[0]], 'error');
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
        this.alertService.alert('Ba??ar??l??!', 'Kod mail adresinize ba??ar??yla g??nderildi.', 'success');
        this.resetPassword.step = 1;
      } else {
        this.alertService.alert('Hata!', 'Kullan??c?? bulunamad??.', 'error');
      }
    });
  }
  changePassword() {
    this.authService.changePassword(this.resetPassword.email, this.resetPassword.code, this.resetPassword.passwordAgain).subscribe(response => {
      if (response.success) {
        this.alertService.alert('Ba??ar??l??!', '??ifreniz ba??ar??yla de??i??tirildi.', 'success');
        this.hidePasswordModal();
      } else {
        this.alertService.alert('Hata!', 'Kodu kontrol ediniz..', 'error');
      }
    });
  }
}
