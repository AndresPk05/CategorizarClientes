from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_item():
    response = client.post(
        "/train",
        json=[{"id":1,"gender":"Male","age":19,"annualIncome":15,"score":39},{"id":2,"gender":"Male","age":21,"annualIncome":15,"score":81},{"id":3,"gender":"Female","age":20,"annualIncome":16,"score":6},{"id":4,"gender":"Female","age":23,"annualIncome":16,"score":77},{"id":5,"gender":"Female","age":31,"annualIncome":17,"score":40},{"id":6,"gender":"Female","age":22,"annualIncome":17,"score":76},{"id":7,"gender":"Female","age":35,"annualIncome":18,"score":6},{"id":8,"gender":"Female","age":23,"annualIncome":18,"score":94},{"id":9,"gender":"Male","age":64,"annualIncome":19,"score":3},{"id":10,"gender":"Female","age":30,"annualIncome":19,"score":72},{"id":11,"gender":"Male","age":67,"annualIncome":19,"score":14},{"id":12,"gender":"Female","age":35,"annualIncome":19,"score":99},{"id":13,"gender":"Female","age":58,"annualIncome":20,"score":15},{"id":14,"gender":"Female","age":24,"annualIncome":20,"score":77},{"id":15,"gender":"Male","age":37,"annualIncome":20,"score":13},{"id":16,"gender":"Male","age":22,"annualIncome":20,"score":79},{"id":17,"gender":"Female","age":35,"annualIncome":21,"score":35},{"id":18,"gender":"Male","age":20,"annualIncome":21,"score":66},{"id":19,"gender":"Male","age":52,"annualIncome":23,"score":29},{"id":20,"gender":"Female","age":35,"annualIncome":23,"score":98},{"id":21,"gender":"Male","age":35,"annualIncome":24,"score":35},{"id":22,"gender":"Male","age":25,"annualIncome":24,"score":73},{"id":23,"gender":"Female","age":46,"annualIncome":25,"score":5},{"id":24,"gender":"Male","age":31,"annualIncome":25,"score":73},{"id":25,"gender":"Female","age":54,"annualIncome":28,"score":14},{"id":26,"gender":"Male","age":29,"annualIncome":28,"score":82},{"id":27,"gender":"Female","age":45,"annualIncome":28,"score":32},{"id":28,"gender":"Male","age":35,"annualIncome":28,"score":61},{"id":29,"gender":"Female","age":40,"annualIncome":29,"score":31},{"id":30,"gender":"Female","age":23,"annualIncome":29,"score":87},{"id":31,"gender":"Male","age":60,"annualIncome":30,"score":4},{"id":32,"gender":"Female","age":21,"annualIncome":30,"score":73},{"id":33,"gender":"Male","age":53,"annualIncome":33,"score":4},{"id":34,"gender":"Male","age":18,"annualIncome":33,"score":92},{"id":35,"gender":"Female","age":49,"annualIncome":33,"score":14},{"id":36,"gender":"Female","age":21,"annualIncome":33,"score":81},{"id":37,"gender":"Female","age":42,"annualIncome":34,"score":17},{"id":38,"gender":"Female","age":30,"annualIncome":34,"score":73},{"id":39,"gender":"Female","age":36,"annualIncome":37,"score":26},{"id":40,"gender":"Female","age":20,"annualIncome":37,"score":75},{"id":41,"gender":"Female","age":65,"annualIncome":38,"score":35},{"id":42,"gender":"Male","age":24,"annualIncome":38,"score":92},{"id":43,"gender":"Male","age":48,"annualIncome":39,"score":36},{"id":44,"gender":"Female","age":31,"annualIncome":39,"score":61},{"id":45,"gender":"Female","age":49,"annualIncome":39,"score":28},{"id":46,"gender":"Female","age":24,"annualIncome":39,"score":65},{"id":47,"gender":"Female","age":50,"annualIncome":40,"score":55},{"id":48,"gender":"Female","age":27,"annualIncome":40,"score":47},{"id":49,"gender":"Female","age":29,"annualIncome":40,"score":42},{"id":50,"gender":"Female","age":31,"annualIncome":40,"score":42},{"id":51,"gender":"Female","age":49,"annualIncome":42,"score":52},{"id":52,"gender":"Male","age":33,"annualIncome":42,"score":60},{"id":53,"gender":"Female","age":31,"annualIncome":43,"score":54},{"id":54,"gender":"Male","age":59,"annualIncome":43,"score":60},{"id":55,"gender":"Female","age":50,"annualIncome":43,"score":45},{"id":56,"gender":"Male","age":47,"annualIncome":43,"score":41},{"id":57,"gender":"Female","age":51,"annualIncome":44,"score":50},{"id":58,"gender":"Male","age":69,"annualIncome":44,"score":46},{"id":59,"gender":"Female","age":27,"annualIncome":46,"score":51},{"id":60,"gender":"Male","age":53,"annualIncome":46,"score":46},{"id":61,"gender":"Male","age":70,"annualIncome":46,"score":56},{"id":62,"gender":"Male","age":19,"annualIncome":46,"score":55},{"id":63,"gender":"Female","age":67,"annualIncome":47,"score":52},{"id":64,"gender":"Female","age":54,"annualIncome":47,"score":59},{"id":65,"gender":"Male","age":63,"annualIncome":48,"score":51},{"id":66,"gender":"Male","age":18,"annualIncome":48,"score":59},{"id":67,"gender":"Female","age":43,"annualIncome":48,"score":50},{"id":68,"gender":"Female","age":68,"annualIncome":48,"score":48},{"id":69,"gender":"Male","age":19,"annualIncome":48,"score":59},{"id":70,"gender":"Female","age":32,"annualIncome":48,"score":47},{"id":71,"gender":"Male","age":70,"annualIncome":49,"score":55},{"id":72,"gender":"Female","age":47,"annualIncome":49,"score":42},{"id":73,"gender":"Female","age":60,"annualIncome":50,"score":49},{"id":74,"gender":"Female","age":60,"annualIncome":50,"score":56},{"id":75,"gender":"Male","age":59,"annualIncome":54,"score":47},{"id":76,"gender":"Male","age":26,"annualIncome":54,"score":54},{"id":77,"gender":"Female","age":45,"annualIncome":54,"score":53},{"id":78,"gender":"Male","age":40,"annualIncome":54,"score":48},{"id":79,"gender":"Female","age":23,"annualIncome":54,"score":52},{"id":80,"gender":"Female","age":49,"annualIncome":54,"score":42},{"id":81,"gender":"Male","age":57,"annualIncome":54,"score":51},{"id":82,"gender":"Male","age":38,"annualIncome":54,"score":55},{"id":83,"gender":"Male","age":67,"annualIncome":54,"score":41},{"id":84,"gender":"Female","age":46,"annualIncome":54,"score":44},{"id":85,"gender":"Female","age":21,"annualIncome":54,"score":57},{"id":86,"gender":"Male","age":48,"annualIncome":54,"score":46},{"id":87,"gender":"Female","age":55,"annualIncome":57,"score":58},{"id":88,"gender":"Female","age":22,"annualIncome":57,"score":55},{"id":89,"gender":"Female","age":34,"annualIncome":58,"score":60},{"id":90,"gender":"Female","age":50,"annualIncome":58,"score":46},{"id":91,"gender":"Female","age":68,"annualIncome":59,"score":55},{"id":92,"gender":"Male","age":18,"annualIncome":59,"score":41},{"id":93,"gender":"Male","age":48,"annualIncome":60,"score":49},{"id":94,"gender":"Female","age":40,"annualIncome":60,"score":40},{"id":95,"gender":"Female","age":32,"annualIncome":60,"score":42},{"id":96,"gender":"Male","age":24,"annualIncome":60,"score":52},{"id":97,"gender":"Female","age":47,"annualIncome":60,"score":47},{"id":98,"gender":"Female","age":27,"annualIncome":60,"score":50},{"id":99,"gender":"Male","age":48,"annualIncome":61,"score":42},{"id":100,"gender":"Male","age":20,"annualIncome":61,"score":49},{"id":101,"gender":"Female","age":23,"annualIncome":62,"score":41},{"id":102,"gender":"Female","age":49,"annualIncome":62,"score":48},{"id":103,"gender":"Male","age":67,"annualIncome":62,"score":59},{"id":104,"gender":"Male","age":26,"annualIncome":62,"score":55},{"id":105,"gender":"Male","age":49,"annualIncome":62,"score":56},{"id":106,"gender":"Female","age":21,"annualIncome":62,"score":42},{"id":107,"gender":"Female","age":66,"annualIncome":63,"score":50},{"id":108,"gender":"Male","age":54,"annualIncome":63,"score":46},{"id":109,"gender":"Male","age":68,"annualIncome":63,"score":43},{"id":110,"gender":"Male","age":66,"annualIncome":63,"score":48},{"id":111,"gender":"Male","age":65,"annualIncome":63,"score":52},{"id":112,"gender":"Female","age":19,"annualIncome":63,"score":54},{"id":113,"gender":"Female","age":38,"annualIncome":64,"score":42},{"id":114,"gender":"Male","age":19,"annualIncome":64,"score":46},{"id":115,"gender":"Female","age":18,"annualIncome":65,"score":48},{"id":116,"gender":"Female","age":19,"annualIncome":65,"score":50},{"id":117,"gender":"Female","age":63,"annualIncome":65,"score":43},{"id":118,"gender":"Female","age":49,"annualIncome":65,"score":59},{"id":119,"gender":"Female","age":51,"annualIncome":67,"score":43},{"id":120,"gender":"Female","age":50,"annualIncome":67,"score":57},{"id":121,"gender":"Male","age":27,"annualIncome":67,"score":56},{"id":122,"gender":"Female","age":38,"annualIncome":67,"score":40},{"id":123,"gender":"Female","age":40,"annualIncome":69,"score":58},{"id":124,"gender":"Male","age":39,"annualIncome":69,"score":91},{"id":125,"gender":"Female","age":23,"annualIncome":70,"score":29},{"id":126,"gender":"Female","age":31,"annualIncome":70,"score":77},{"id":127,"gender":"Male","age":43,"annualIncome":71,"score":35},{"id":128,"gender":"Male","age":40,"annualIncome":71,"score":95},{"id":129,"gender":"Male","age":59,"annualIncome":71,"score":11},{"id":130,"gender":"Male","age":38,"annualIncome":71,"score":75},{"id":131,"gender":"Male","age":47,"annualIncome":71,"score":9},{"id":132,"gender":"Male","age":39,"annualIncome":71,"score":75},{"id":133,"gender":"Female","age":25,"annualIncome":72,"score":34},{"id":134,"gender":"Female","age":31,"annualIncome":72,"score":71},{"id":135,"gender":"Male","age":20,"annualIncome":73,"score":5},{"id":136,"gender":"Female","age":29,"annualIncome":73,"score":88},{"id":137,"gender":"Female","age":44,"annualIncome":73,"score":7},{"id":138,"gender":"Male","age":32,"annualIncome":73,"score":73},{"id":139,"gender":"Male","age":19,"annualIncome":74,"score":10},{"id":140,"gender":"Female","age":35,"annualIncome":74,"score":72},{"id":141,"gender":"Female","age":57,"annualIncome":75,"score":5},{"id":142,"gender":"Male","age":32,"annualIncome":75,"score":93},{"id":143,"gender":"Female","age":28,"annualIncome":76,"score":40},{"id":144,"gender":"Female","age":32,"annualIncome":76,"score":87},{"id":145,"gender":"Male","age":25,"annualIncome":77,"score":12},{"id":146,"gender":"Male","age":28,"annualIncome":77,"score":97},{"id":147,"gender":"Male","age":48,"annualIncome":77,"score":36},{"id":148,"gender":"Female","age":32,"annualIncome":77,"score":74},{"id":149,"gender":"Female","age":34,"annualIncome":78,"score":22},{"id":150,"gender":"Male","age":34,"annualIncome":78,"score":90},{"id":151,"gender":"Male","age":43,"annualIncome":78,"score":17},{"id":152,"gender":"Male","age":39,"annualIncome":78,"score":88},{"id":153,"gender":"Female","age":44,"annualIncome":78,"score":20},{"id":154,"gender":"Female","age":38,"annualIncome":78,"score":76},{"id":155,"gender":"Female","age":47,"annualIncome":78,"score":16},{"id":156,"gender":"Female","age":27,"annualIncome":78,"score":89},{"id":157,"gender":"Male","age":37,"annualIncome":78,"score":1},{"id":158,"gender":"Female","age":30,"annualIncome":78,"score":78},{"id":159,"gender":"Male","age":34,"annualIncome":78,"score":1},{"id":160,"gender":"Female","age":30,"annualIncome":78,"score":73},{"id":161,"gender":"Female","age":56,"annualIncome":79,"score":35},{"id":162,"gender":"Female","age":29,"annualIncome":79,"score":83},{"id":163,"gender":"Male","age":19,"annualIncome":81,"score":5},{"id":164,"gender":"Female","age":31,"annualIncome":81,"score":93},{"id":165,"gender":"Male","age":50,"annualIncome":85,"score":26},{"id":166,"gender":"Female","age":36,"annualIncome":85,"score":75},{"id":167,"gender":"Male","age":42,"annualIncome":86,"score":20},{"id":168,"gender":"Female","age":33,"annualIncome":86,"score":95},{"id":169,"gender":"Female","age":36,"annualIncome":87,"score":27},{"id":170,"gender":"Male","age":32,"annualIncome":87,"score":63},{"id":171,"gender":"Male","age":40,"annualIncome":87,"score":13},{"id":172,"gender":"Male","age":28,"annualIncome":87,"score":75},{"id":173,"gender":"Male","age":36,"annualIncome":87,"score":10},{"id":174,"gender":"Male","age":36,"annualIncome":87,"score":92},{"id":175,"gender":"Female","age":52,"annualIncome":88,"score":13},{"id":176,"gender":"Female","age":30,"annualIncome":88,"score":86},{"id":177,"gender":"Male","age":58,"annualIncome":88,"score":15},{"id":178,"gender":"Male","age":27,"annualIncome":88,"score":69},{"id":179,"gender":"Male","age":59,"annualIncome":93,"score":14},{"id":180,"gender":"Male","age":35,"annualIncome":93,"score":90},{"id":181,"gender":"Female","age":37,"annualIncome":97,"score":32},{"id":182,"gender":"Female","age":32,"annualIncome":97,"score":86},{"id":183,"gender":"Male","age":46,"annualIncome":98,"score":15},{"id":184,"gender":"Female","age":29,"annualIncome":98,"score":88},{"id":185,"gender":"Female","age":41,"annualIncome":99,"score":39},{"id":186,"gender":"Male","age":30,"annualIncome":99,"score":97},{"id":187,"gender":"Female","age":54,"annualIncome":101,"score":24},{"id":188,"gender":"Male","age":28,"annualIncome":101,"score":68},{"id":189,"gender":"Female","age":41,"annualIncome":103,"score":17},{"id":190,"gender":"Female","age":36,"annualIncome":103,"score":85},{"id":191,"gender":"Female","age":34,"annualIncome":103,"score":23},{"id":192,"gender":"Female","age":32,"annualIncome":103,"score":69},{"id":193,"gender":"Male","age":33,"annualIncome":113,"score":8},{"id":194,"gender":"Female","age":38,"annualIncome":113,"score":91},{"id":195,"gender":"Female","age":47,"annualIncome":120,"score":16},{"id":196,"gender":"Female","age":35,"annualIncome":120,"score":79},{"id":197,"gender":"Female","age":45,"annualIncome":126,"score":28},{"id":198,"gender":"Male","age":32,"annualIncome":126,"score":74},{"id":199,"gender":"Male","age":32,"annualIncome":137,"score":18},{"id":200,"gender":"Male","age":30,"annualIncome":137,"score":83}],
    )
    assert response.status_code == 200