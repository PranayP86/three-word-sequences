import pytest
from challenge.app import load_text, replace_escapes, process_trigrams, print_words

@pytest.mark.parametrize("test_input, expected", [
    ('\\n', []),
    (r'\t', []),
    ('“Hello!”', ['hello']),
    ('''"don't"''', ["don't"]),
    ("""ShoUlD'vE nOt bEen CaPITalIzED""", ["should've", 'not', 'been', 'capitalized']),
])
def test_load_text(test_input, expected):
    assert load_text(input_text=test_input, stdin=True) == expected
    
@pytest.mark.parametrize("test_input, expected", [
    ('\\v', []),
    ('\\b', []),
    (r'\\', []),
    ('''“Let's run some tests.”, Lew said.''', ["Let's", 'run', 'some', 'tests', 'Lew', 'said']),
    (r"""Don't know if i\\tt's work\\ning..., maybe it is?""", ["Don't", 'know', 'if', "it's", 'working', 'maybe', 'it', 'is']),
    ('''"We're good; it works!"''', ["We're", 'good', 'it', 'works']),
])
def test_replace_escapes(test_input, expected):
    assert replace_escapes(test_input) == expected
    
@pytest.mark.parametrize("test_input, expected", [
    (['three', 'four', 'one', 'two', 'three', 'four', 'one', 'two', 'three', 'three', 'three', 'four', 'one'], 
     [(('three', 'four', 'one'), 3), (('four', 'one', 'two'), 2), (('one', 'two', 'three'), 2)]),
    (['same', 'same', 'same', 'same', 'same', 'same', 'same', 'same'], [(('same', 'same', 'same'), 6)]),
])
def test_process_trigrams(test_input, expected):
    assert process_trigrams(test_input) == expected

def test_print_words(capfd):
    test_input = (['most', 'common', 'phrase', 'hi', 'there', 'friend', 'most', 'hi', 'there', 'most', 'common', 'phrase'])
    print_words(test_input)
    captured = capfd.readouterr()
    assert captured.out == "most common phrase  -  2\n"