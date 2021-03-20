import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Role } from 'src/app/core/models/role.model';
import { RoleService } from 'src/app/core/services/role.service';
import { LoadingService } from './../../../../core/services/loading.service';

@Component({
  selector: 'app-upsert-role',
  templateUrl: './upsert-role.component.html',
  styleUrls: ['./upsert-role.component.scss']
})
export class UpsertRoleComponent implements OnInit {
  role = new Role();
  permissions: { key: string; name: string }[] = [];
  notifications: { key: string; name: string }[] = []
  constructor(
    private loadingService: LoadingService,
    private roleService: RoleService,
    private route: ActivatedRoute,
    private router: Router
  ) { }

  ngOnInit(): void {
    if (this.route.snapshot.params.id) {
      this.getRole();
    }
    this.getPermissions();
    this.getNotifications();
  }

  getRole() {
    this.loadingService.setLoading(true);
    this.roleService.getRole(this.route.snapshot.params.id).subscribe(response => {
      if (response.success) {
        this.role = response.data;
      }
      this.loadingService.setLoading(false);
    })
  }

  getPermissions() {
    this.loadingService.setLoading(true);
    this.roleService.getCompanyPermissions().subscribe(response => {
      if (response.success) {
        this.permissions = response.data;
      }
      this.loadingService.setLoading(false);
    })
  }

  getNotifications() {
    this.loadingService.setLoading(true);
    this.roleService.getCompanyNotifications().subscribe(response => {
      if (response.success) {
        this.notifications = response.data;
      }
      this.loadingService.setLoading(false);
    })
  }

  save() {
    this.roleService.upsertRole(this.role).subscribe(response => {
      if (response.success) {
        this.router.navigate(['/roles']);
      }
    })

  }


}
