import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from '../config';
import { User } from './../models/user.model';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(
    private httpClient: HttpClient
  ) { }

  getUsers(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/user').pipe(
      map(res => res)
    )
  }

  getById(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/user/single/' + id).pipe(
      map(res => res)
    );
  }

  createUser(user: User): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/user/createUser', user).pipe(
      map(res => res)
    )
  }

  updateUser(user: User): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/user/updateUser', user).pipe(
      map(res => res)
    )
  }

  getEngineers(neighborhood?: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/user/engineers?neighborhood=' + neighborhood || 'all').pipe(
      map(res => res)
    )
  }

  getLicenseEngineers(neighborhood?: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/user/licenseEngineers?neighborhood=' + neighborhood || 'all').pipe(
      map(res => res)
    )
  }

  getSettlementEngineers(neighborhood?: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/user/settlementEngineers?neighborhood=' + neighborhood || 'all').pipe(
      map(res => res)
    )
  }

  changePassword(body: { userId: string, password: string }): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/user/changePassword', body).pipe(
      map(res => res)
    );
  }
}
