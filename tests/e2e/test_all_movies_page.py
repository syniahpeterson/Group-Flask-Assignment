# TODO: Feature 1
def test_list_all_movies(test_app):
    test_app.post('/movies',data=dict(title="Up", director="Pete Docter", rating="3"))
    test_app.post('/movies', data=dict(title="Inside Out",director="Pete Docter", rating="4"))
    test_app.post('/movies', data=dict(title="Rio", director="Carlos Saldanha", rating="1"))
    response = test_app.get('/movies')
    assert b"<tr><th>Up</th><td>Pete Docter</td><td>3/5</td></tr>" in response.data
    assert b"<tr><th>Inside Out 2</th><td>Pete Docter</td><td>4/5</td></tr>" in response.data
    assert b"<tr><th>Rio</th><td>Carlos Saldanha</td><td>1/5</td></tr>" in response.data