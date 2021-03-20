import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/core/services/auth.service';
import { RoleService } from './core/services/role.service';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'Certificiency';
  year = new Date().getFullYear();
  constructor(
    private authService: AuthService,
    private router: Router,
    private roleService: RoleService
  ) {

  }
  async ngOnInit() {
    const token = this.authService.getToken();
    if (!token) {
      this.router.navigate(['/login']);
    } else {
      await this.roleService.getCurrentUserRoles().toPromise();
    }
  }
}
