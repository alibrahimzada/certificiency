import { AfterViewInit, Directive, ElementRef, Input } from '@angular/core';
import { RoleService } from './../services/role.service';

@Directive({
  selector: '[appIsVisibleForUser]'
})
export class IsVisibleForUserDirective implements AfterViewInit {

  @Input('appIsVisibleForUser') permission: string;
  @Input('roles') roles: string[]
  constructor(
    private el: ElementRef,
    private roleService: RoleService
  ) {

  }

  ngAfterViewInit(): void {
    const elem = this.el.nativeElement as HTMLElement;
    if (!this.roleService.userHavePermission(this.permission)) {
      elem.remove();
    }
  }

}
