import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { API_ENDPOINT } from './../config';
import { Notification } from './../models/notification.model';

@Injectable({
  providedIn: 'root'
})
export class NotificationService {

  constructor(
    private http: HttpClient
  ) { }

  getNotificationCount(): Observable<any> {
    return this.http.get(API_ENDPOINT + '/notification/notificationCount').pipe(
      map(res => res)
    )
  }

  getNotifications(): Observable<any> {
    return this.http.get(API_ENDPOINT + '/notification/notifications').pipe(
      map(res => res)
    )
  }

  setNotificationAsRead(id: string): Observable<any> {
    return this.http.get(API_ENDPOINT + '/notification/setNotificationAsRead/' + id).pipe(
      map(res => res)
    )
  }

  send(notification: Notification) {
    return this.http.post(API_ENDPOINT + '/notification/send', notification).pipe(
      map(res => res)
    );
  }

  sendToRoles(notification: Notification, sendToRoles: string[]) {
    return this.http.post(API_ENDPOINT + '/notification/sendToRoles', { notification, sendToRoles }).pipe(
      map(res => res)
    );
  }

  sendToKeys(data: {
    notificationKey: string,
    notification: { content: string, entity: string, entityId: string },
  }) {
    return this.http.post(API_ENDPOINT + '/notification/sendToKey', data).pipe(
      map(res => res)
    );
  }
}
