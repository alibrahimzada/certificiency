import { HttpEvent, HttpHandler, HttpInterceptor, HttpRequest } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { AuthService } from 'src/app/core/services/auth.service';

@Injectable()
export class GeneralInterceptor implements HttpInterceptor {

  constructor(
    private authService: AuthService
  ) { }

  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    if (request.url.includes('auth')) {
      return next.handle(request);
    }
    const newReq = request.clone({ headers: request.headers.append('authorization', `Bearer ${this.authService.getToken()}`) })
    return next.handle(newReq);
  }
}
