import { Component, OnInit } from '@angular/core';
import { LoadingService } from './../../core/services/loading.service';
import { RoleService } from './../../core/services/role.service';

@Component({
  selector: 'app-roles',
  templateUrl: './roles.component.html',
  styleUrls: ['./roles.component.scss']
})
export class RolesComponent implements OnInit {
  roles: any[] = [];
  constructor(
    private roleService: RoleService,
    private loadingService: LoadingService
  ) { }

  ngOnInit(): void {
    this.getRoles();
  }

  getRoles() {
    this.loadingService.setLoading(true);
    this.roleService.getRoles().subscribe(response => {
      if (response.success) {
        this.roles = response.data;
      }
      this.loadingService.setLoading(false);
    })
  }

}
