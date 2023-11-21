import { TestBed } from '@angular/core/testing';

import { FileCsvService } from './file-csv.service';

describe('FileCsvService', () => {
  let service: FileCsvService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FileCsvService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
