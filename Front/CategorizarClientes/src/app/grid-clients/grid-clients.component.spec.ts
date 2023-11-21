import { ComponentFixture, TestBed } from '@angular/core/testing';

import { GridClientsComponent } from './grid-clients.component';

describe('GridClientsComponent', () => {
  let component: GridClientsComponent;
  let fixture: ComponentFixture<GridClientsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [GridClientsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(GridClientsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
