import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { Role } from '../models/role.model';
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
    private httpClient: HttpClient,
  ) { }

  getRoles(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/role/all').pipe(
      map(res => res)
    )
  }

  getById(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/role/' + id).pipe(
      map(res => res)
    );
  }

  createRole(role: Role): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/role/', role).pipe(
      map(res => res)
    )
  }

  updateRole(role: Role): Observable<any> {
    return this.httpClient.put(API_ENDPOINT + '/role/', role).pipe(
      map(res => res)
    )
  }

  deleteRole(id: string): Observable<any> {
    return this.httpClient.delete(API_ENDPOINT + '/role/' + id).pipe(
      map(res => res)
    )
  }

  getCompanyPermissions(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/role/companyPermissions').pipe(map(res => res))
  }

  getCurrentUserRoles(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/role/currentUserRoles').pipe(map((res: any) => {
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

}
