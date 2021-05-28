import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpsertEventComponent } from './upsert-event.component';

describe('UpsertEventComponent', () => {
  let component: UpsertEventComponent;
  let fixture: ComponentFixture<UpsertEventComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpsertEventComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpsertEventComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
