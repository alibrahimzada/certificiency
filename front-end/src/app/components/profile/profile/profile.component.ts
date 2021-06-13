import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/core/models/user.model';
import { AlertService } from 'src/app/core/services/alert.service';
import { AuthService } from 'src/app/core/services/auth.service';
import { LoadingService } from 'src/app/core/services/loading.service';
import { RoleService } from 'src/app/core/services/role.service';
import { UserService } from 'src/app/core/services/user.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.scss']
})
export class ProfileComponent implements OnInit {
  user: User = new User();
  userChange = {
    first_name: '',
    last_name: '',
    email: ''
  }
  passwordChange = {
    old_password: '',
    new_password: '',
    confirm_new_password: ''
  }
  stats: any;
  constructor(private authService: AuthService,
    private userService: UserService,
    private alertService: AlertService,
    private loadingService: LoadingService,
    public roleService: RoleService) { }

  ngOnInit(): void {
    this.user = this.authService.getCurrentUser();
    console.log(this.user);
    this.userChange.first_name = this.user.first_name;
    this.userChange.last_name = this.user.last_name;
    this.userChange.email = this.user.email;
    this.getStats();
  }

  updateUser() {
    this.loadingService.setLoading(true);
    if (this.user.user_id) {
      this.userService.updateMyProfile(this.userChange).subscribe(response => {
        if (response.success) {
          this.alertService.alert('Success!', 'Your profile is updated! <b>Your changes will be updated once you logout and login!</b>', 'success');
        } else {
          this.alertService.alert('Error!', 'Your profile could not update', 'error');
        }
        this.loadingService.setLoading(false);
      })
    }
  }

  changePassword() {
    this.loadingService.setLoading(true);
    this.userService.changePassword(this.passwordChange).subscribe(response => {
      if (response.success) {
        this.alertService.alert('Success!', 'Your password is updated', 'success');
      } else {
        this.alertService.alert('Error!', 'Your password could not update', 'error');
      }
      this.loadingService.setLoading(false);
    })
  }

  getStats(){
    this.userService.getStatsById(this.user.user_id).subscribe(response => {
      if (response.success) {
        this.stats = response.data;
        console.log(this.stats);
      }
      else {
        this.alertService.alert('Error!', 'Could not get statistics of the user!', 'error');
      }
    })
  }

}
