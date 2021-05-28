import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { UpsertEventCategoryComponent } from './upsert-event-category.component';

describe('UpsertEventCategoryComponent', () => {
  let component: UpsertEventCategoryComponent;
  let fixture: ComponentFixture<UpsertEventCategoryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ UpsertEventCategoryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(UpsertEventCategoryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
