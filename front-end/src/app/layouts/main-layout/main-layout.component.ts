import { AfterViewInit, Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Subscription } from 'rxjs';
import { User } from './../../core/models/user.model';
import { AuthService } from './../../core/services/auth.service';
import { NotificationService } from './../../core/services/notification.service';
import { RoleService } from './../../core/services/role.service';

@Component({
  selector: 'app-main-layout',
  templateUrl: './main-layout.component.html',
  styleUrls: ['./main-layout.component.scss']
})
export class MainLayoutComponent implements OnInit, AfterViewInit {
  year = new Date().getFullYear();
  user: User = new User();
  notificationCount = 0;
  notifications = [];
  route$: Subscription;
  interval = null;
  constructor(
    private authService: AuthService,
    private notificationService: NotificationService,
    private router: Router,
    public roleService: RoleService
  ) { }

  ngOnInit(): void {
    this.user = this.authService.getCurrentUser();
    console.log(this.user);
  }

  ngAfterViewInit() {
    const onResize = () => {
      const headerHeight = document.getElementById('kt_header').clientHeight;
      const footerHeight = document.getElementById('kt_footer').clientHeight;
      document.getElementById('kt_content').style.minHeight = (document.body.clientHeight - (headerHeight + footerHeight)) + 'px'
    }
    window.onresize = onResize;
    onResize();
  }

  logout() {
    this.authService.logout();
  }

}
