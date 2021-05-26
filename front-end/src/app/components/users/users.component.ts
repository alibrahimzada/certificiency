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
  }

  ngOnInit(): void {
    this.getUsers();
  }

  getUsers(){
    this.userService.getUsers().subscribe(response => {
      if (response.success){
        this.users = response.data;
        console.log(this.users);
      }
      else {
        this.alertService.alert("Error!", "Users cannot be fetched!", "error");
      }
    });
  }

}
