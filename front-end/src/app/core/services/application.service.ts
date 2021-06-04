import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from '../config';
import { Application } from './../models/application.model';

@Injectable({
  providedIn: 'root'
})
export class ApplicationService {

  constructor(
    private httpClient: HttpClient
  ) { }

  getApplications(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/application/all').pipe(
      map(res => res)
    )
  }

  getById(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/application/' + id).pipe(
      map(res => res)
    );
  }

  getApplicationsByEventId(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/application/'+ id + '/applications').pipe(
      map(res => res)
    )
  }

  createApplication(application: Application): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/application/insert', application).pipe(
      map(res => res)
    )
  }

  updateApplication(application: Application): Observable<any> {
    return this.httpClient.put(API_ENDPOINT + '/application/update', application).pipe(
      map(res => res)
    )
  }

  updateStatus(application_id: string, application_status: number): Observable<any> {
    return this.httpClient.put(API_ENDPOINT + '/application/status', {application_id, application_status}).pipe(
      map(res => res)
    )
  }

  deleteApplication(id: string): Observable<any> {
    return this.httpClient.delete(API_ENDPOINT + '/application/delete/' + id).pipe(
      map(res => res)
    )
  }  
}
