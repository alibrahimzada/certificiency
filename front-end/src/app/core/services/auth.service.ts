import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from '../config';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient,
    private router: Router
  ) { }

  login(body: { username, password }): Observable<any> {
    return this.http.post(API_ENDPOINT + '/auth/login', body).pipe(
      map(res => res)
    )
  }

  helloWorld(): Observable<any> {
    return this.http.get(API_ENDPOINT).pipe(
      map(res => res)
    )
  }

  saveUserToLocalStorage(response: { token: string, user: any }) {
    localStorage.setItem('token', response.token);
    localStorage.setItem('user', JSON.stringify(response.user));
  }

  getToken() {
    return localStorage.getItem('token') || null;
  }

  getCurrentUser() {
    return localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')) : null;
  }

  logout() {
    localStorage.clear();
    this.router.navigate(['/login']);
  }

  sendCode(email: string): Observable<{ success: boolean }> {
    return this.http.post<any>(API_ENDPOINT + '/auth/forgotPassword', { email }).pipe(
      map(res => res)
    );
  }

  checkCode(email: string, code: string): Observable<{ success: boolean }> {
    return this.http.post<any>(API_ENDPOINT + '/auth/checkCode', { email, code }).pipe(
      map(res => res)
    );
  }

  changePassword(email: string, code: string, password: string): Observable<{ success: boolean }> {
    return this.http.post<any>(API_ENDPOINT + '/auth/changePassword', { email, code, password }).pipe(
      map(res => res)
    );
  }
}
