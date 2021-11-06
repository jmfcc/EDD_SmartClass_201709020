import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NuevoApunteComponent } from './nuevo-apunte.component';

describe('NuevoApunteComponent', () => {
  let component: NuevoApunteComponent;
  let fixture: ComponentFixture<NuevoApunteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ NuevoApunteComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(NuevoApunteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
