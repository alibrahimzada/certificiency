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
    return this.httpClient.get(API_ENDPOINT + '/user/all').pipe(
      map(res => res)
    )
  }

  getById(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/user/' + id).pipe(
      map(res => res)
    );
  }

  getHelloWorld(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT).pipe(
      map(res => res)
    );
  }

  createUser(user: User): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/user/insert', user).pipe(
      map(res => res)
    )
  }

  updateUser(user: User): Observable<any> {
    return this.httpClient.put(API_ENDPOINT + '/user/update', user).pipe(
      map(res => res)
    )
  }

  deleteUser(id: string): Observable<any> {
    return this.httpClient.delete(API_ENDPOINT + '/user/delete/' + id).pipe(
      map(res => res)
    )
  }  
}
