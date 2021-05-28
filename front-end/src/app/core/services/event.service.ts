import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from '../config';
import { Event } from './../models/event.model';

@Injectable({
  providedIn: 'root'
})
export class EventService {

  constructor(
    private httpClient: HttpClient
  ) { }

  getEvents(): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/event/all').pipe(
      map(res => res)
    )
  }

  getById(id: string): Observable<any> {
    return this.httpClient.get(API_ENDPOINT + '/event/' + id).pipe(
      map(res => res)
    );
  }

  createEvent(event: Event): Observable<any> {
    return this.httpClient.post(API_ENDPOINT + '/event/insert', event).pipe(
      map(res => res)
    )
  }

  updateEvent(event: Event): Observable<any> {
    return this.httpClient.put(API_ENDPOINT + '/event/update', event).pipe(
      map(res => res)
    )
  }

  deleteEvent(id: string): Observable<any> {
    return this.httpClient.delete(API_ENDPOINT + '/event/delete/' + id).pipe(
      map(res => res)
    )
  }  
}