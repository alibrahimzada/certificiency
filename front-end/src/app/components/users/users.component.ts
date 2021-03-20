import { Component, OnInit } from '@angular/core';
import { User } from './../../core/models/user.model';
import { AlertService } from './../../core/services/alert.service';
import { GeneralApiService } from './../../core/services/general-api.service';
import { LoadingService } from './../../core/services/loading.service';
import { RoleService } from './../../core/services/role.service';
import { UserService } from './../../core/services/user.service';
declare const $: any;
@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent implements OnInit {
  users = [];
  roles = [];
  selectedUserId = null;
  newPasswordBody = {
    password: '',
    confirm: ''
  }
  constructor(
    private userService: UserService,
    private alertService: AlertService,
    private loadingService: LoadingService,
    private roleService: RoleService,
    private apiService: GeneralApiService
  ) {
    this.roleService.getRoles().subscribe(response => {
      if (response.success) {
        this.roles = response.data;
      }
    })
  }

  ngOnInit(): void {
    this.loadingService.setLoading(true);
    this.getUsers();
  }

  getUsers() {
    this.userService.getUsers().subscribe(response => {
      if (response.success) {
        this.users = response.data;
      }
      else {
        this.alertService.alert('Hata!', 'Kullanıcılar alınamadı.', 'error');
      }
      this.loadingService.setLoading(false);
    });
  }

  getRoleName(roleId: string) {
    const role = this.roles.find(x => x.id === roleId);
    return role ? role.roleName : '-';
  }

  showChangePasswordModal(user: User) {
    this.selectedUserId = user.id;
    $('.modal').modal('show')
  }

  hideChangePasswordModal() {
    $('.modal').modal('hide')
    this.newPasswordBody = {
      password: '',
      confirm: ''
    }
    this.selectedUserId = null;
  }

  changePassword() {
    if (this.newPasswordBody.password !== this.newPasswordBody.confirm) {
      return this.alertService.alert('Hata!', 'Şifreler uyuşmuyor', 'error');
    }
    this.userService.changePassword({
      password: this.newPasswordBody.password,
      userId: this.selectedUserId
    }).subscribe(response => {
      if (response.success) {
        this.alertService.notification('Başarılı!', 'Şifre başarıyla güncellendi', 'success');
        this.hideChangePasswordModal();
      } else {
        this.alertService.notification('Hata!', 'Şifre güncellenemedi', 'error');
      }
    })
  }

  deleteUser(id: string, email: string) {
    const x = confirm(email + ' kullanıcısını silmek istediğinize emin misiniz?');
    if (x) {
      this.apiService.deleteRecord(id, 'user').subscribe(response => {
        if (response.success) {
          this.getUsers();
        }
      })
    }
  }
}
