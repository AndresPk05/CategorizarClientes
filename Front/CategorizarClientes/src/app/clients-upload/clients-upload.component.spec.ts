import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ClientsUploadComponent } from './clients-upload.component';

describe('ClientsUploadComponent', () => {
  let component: ClientsUploadComponent;
  let fixture: ComponentFixture<ClientsUploadComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ClientsUploadComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(ClientsUploadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
