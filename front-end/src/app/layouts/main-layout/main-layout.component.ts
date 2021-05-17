import { AfterViewInit, Component, OnDestroy, OnInit } from '@angular/core';
import { NavigationStart, Router } from '@angular/router';
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
export class MainLayoutComponent implements OnInit, AfterViewInit, OnDestroy {
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
    this.user.first_name = "Beyza";
    this.user.last_name = "Aydogan";
    // this.user = this.authService.getCurrentUser();
    // this.refreshNotifications();
    // this.route$ = this.router.events.subscribe(event => {
    //   if (event instanceof NavigationStart) {
    //     this.refreshNotifications();
    //   }
    // });
    // this.interval = setInterval(() => {
    //   this.refreshNotifications();
    // }, 10000)
  }

  refreshNotifications() {
    if (this.authService.getToken()) {
      this.notificationService.getNotificationCount().subscribe(response => {
        if (response.success) {
          this.notificationCount = response.data.notificationCount;
        }
      });
      this.notificationService.getNotifications().subscribe(response => {
        if (response.success) {
          this.notifications = response.data;
        }
      });
    }
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

  getUrl(entity: string, id: string) {
    switch (entity) {
      case 'Report': {
        return ['/field-report/detail/' + id]
      }
      case 'License': {
        return ['/license/detail/' + id]
      }
      case 'Settlement': {
        return ['/settlement/detail/' + id]
      }
      case 'Demand': {
        return ['/demand/detail/' + id]
      }
      default: {
        return null;
      }
    }
  }

  navigateToNotification(e: any, notification: any) {
    e.preventDefault();
    const url = this.getUrl(notification.entity, notification.entityId)
    this.notificationService.setNotificationAsRead(notification.id).subscribe(response => {
      this.refreshNotifications();
      if (url) {
        this.router.navigate(url);
      }
    });
  }

  ngOnDestroy() {
    this.route$.unsubscribe();
    if (this.interval) {
      clearInterval(this.interval)
    }
  }

}
