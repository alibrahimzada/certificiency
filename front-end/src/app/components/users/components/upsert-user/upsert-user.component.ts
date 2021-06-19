import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { User } from './../../../../core/models/user.model';
import { AlertService } from './../../../../core/services/alert.service';
import { LoadingService } from './../../../../core/services/loading.service';
import { RoleService } from './../../../../core/services/role.service';
import { UserService } from './../../../../core/services/user.service';

@Component({
  selector: 'app-upsert-user',
  templateUrl: './upsert-user.component.html',
  styleUrls: ['./upsert-user.component.scss']
})
export class UpsertUserComponent implements OnInit {
  user = new User();
  roles = [];
  constructor(
    private userService: UserService,
    private loadingService: LoadingService,
    private alertService: AlertService,
    private roleService: RoleService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.roleService.getRoles().subscribe(response => {
      if (response.success) {
        this.roles = response.data;
        this.user.user_type = 2;
        console.log(response);
      }
    });
    if (this.route.snapshot.params.id) {
      this.userService.getById(this.route.snapshot.params.id).subscribe(response => {
        if (response.success) {
          this.user = response.data;
        }
      })
    }
  }

  save() {
    // this.loadingService.setLoading(true);
    if (this.user.user_id) {
      const { password, ...rest } = this.user;
      this.userService.updateUser(rest as any).subscribe(response => {
        if (response.success) {
          this.alertService.notification('Başarılı!', 'Personel başarıyla güncellendi', 'success');
          this.router.navigate(['/users']);
        } else {
          this.alertService.notification('Hata!', 'Personel güncellenemedi', 'error');
        }
        this.loadingService.setLoading(false);
      })
    } else {
      this.userService.createUser(this.user).subscribe(response => {
        const { success } = response;
        if (success) {
          this.alertService.notification('Başarılı!', 'Kullanıcı başarıyla eklendi', 'success');
          this.router.navigate(['/users']);
        } else {
          this.alertService.notification('Hata!', 'Personel eklenemedi', 'error');
        }
        this.loadingService.setLoading(false);
      })
    }
  }

}
