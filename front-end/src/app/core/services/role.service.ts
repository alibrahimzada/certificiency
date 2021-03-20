import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from './../config';

@Injectable({
  providedIn: 'root',
})
export class RoleService {
  currentUserRole = {
    roleName: '',
    permissions: []
  };
  roleName = '';
  constructor(
    private http: HttpClient,
  ) { }

  getRoles(): Observable<any> {
    return this.http.get(API_ENDPOINT + '/role/roles').pipe(map(res => res));
  }

  getCompanyPermissions(): Observable<any> {
    return this.http.get(API_ENDPOINT + '/role/companyPermissions').pipe(map(res => res))
  }

  getCompanyNotifications(): Observable<any> {
    return this.http.get(API_ENDPOINT + '/role/companyNotifications').pipe(map(res => res))
  }

  getRole(id: string): Observable<any> {
    return this.http.get(API_ENDPOINT + '/role/single/' + id).pipe(map(res => res));
  }

  getCurrentUserRoles(): Observable<any> {
    return this.http.get(API_ENDPOINT + '/role/currentUserRoles').pipe(map((res: any) => {
      this.currentUserRole = res.data;
      this.roleName = res.data.roleName;
      return res;
    }));
  }

  visibleForCurrentUser(roles: string[]) {
    const result = roles.indexOf(this.roleName) !== -1;
    return result;
  }

  userHavePermission(permission: string) {
    return this.currentUserRole && this.currentUserRole.permissions && this.currentUserRole.permissions.findIndex(x => x.key === permission) !== -1
  }

  upsertRole(role: any): Observable<any> {
    return this.http.post(API_ENDPOINT + '/role/upsertRole', role).pipe(map(res => res));
  }
}
