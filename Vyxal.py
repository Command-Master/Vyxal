# Python modules
import copy
from datetime import date
from datetime import datetime as dt
import functools
import hashlib
import itertools
import math
import random
import string
import time
import urllib.request
import warnings
import base64

# Vyxal modules
import commands
import encoding
import utilities
import VyParse
import words

# Pipped modules

try:
    import numpy
    import regex
    import sympy
except:
    import os
    os.system("pip install -r requirements.txt --quiet --disable-pip-version-check")

# Generic type constants
Number = "NUMBER"
Iterable = "ITERABLE"
Function = type(lambda: None)

Python_Generator = type(i for i in(0,)) # https://chat.stackexchange.com/transcript/message/57555979#57555979

NEWLINE = "\n"
ONE_TWO_EIGHT_KB = 1024000

# Execution variables
context_level = 0
context_values = [0]
global_stack = []
input_level = 0
inputs = []
input_values = {0: [inputs, 0]} # input_level: [source, input_index]
keg_mode = False
number_iterable = list
raw_strings = False
online_version = False
output = ""
printed = False
register = 0
retain_items = False
reverse_args = False
safe_mode = False # You may want to have safe evaluation but not be online.
stack = []
this_function = lambda x: VY_print(stack)or x

MAP_START = 1
MAP_OFFSET = 1
_join = False
_vertical_join = False
use_encoding = False
FIRST_100_FACTORIALS = (0x1,0x1,0x2,0x6,0x18,0x78,0x2d0,0x13b0,0x9d80,0x58980,0x375f00,0x2611500,0x1c8cfc00,0x17328cc00,0x144c3b2800,0x13077775800,
0x130777758000,0x1437eeecd8000,0x16beecca730000,0x1b02b9306890000,0x21c3677c82b40000,0x2c5077d36b8c40000,0x3ceea4c2b3e0d80000,0x57970cd7e2933680000,
0x83629343d3dcd1c00000,0xcd4a0619fb0907bc00000,0x14d9849ea37eeac91800000,0x232f0fcbb3e62c3358800000,0x3d925ba47ad2cd59dae000000,0x6f99461a1e9e1432dcb6000000,
0xd13f6370f96865df5dd54000000,0x1956ad0aae33a4560c5cd2c000000,0x32ad5a155c6748ac18b9a580000000,0x688589cc0e9505e2f2fee5580000000,
0xde1bc4d19efcac82445da75b00000000,0x1e5dcbe8a8bc8b95cf58cde17100000000,0x44530acb7ba83a111287cf3b3e400000000,0x9e0008f68df506477ada0f38fff400000000,
0x1774015499125eee9c3c5e4275fe3800000000,0x392ac33e351cc7659cd325c1ff9ba8800000000,0x8eeae81b84c7f27e080fde64ff05254000000000,
0x16e39f2c684405d62f4a8a9e2cd7d2f74000000000,0x3c1581d491b28f523c23abdf35b689c908000000000,0xa179cceb478fe12d019fdde7e05a924c458000000000,
0x1bc0ef38704cbab3bc477a23da8f91251bf20000000000,0x4e0ea0cebbd7cd1981890784d6b3c8385e98a0000000000,0xe06a0e525c0c6da95469f59de944dfa20ff6cc0000000000,
0x293378a11ee64822167f7417fdd3a50ec0ee4f740000000000,0x7b9a69e35cb2d866437e5c47f97aef2c42caee5c00000000000,
0x17a88e4484be3b6b92eb2fa9c6c087c778c8d79f9c00000000000,0x49eebc961ed279b02b1ef4f28d19a84f5973a1d2c7800000000000,
0xeba8f91e823ee3e18972acc521c1c87ced2093cfdbe800000000000,0x2fde529a3274c649cfeb4b180adb5cb9602a9e0638ab2000000000000,
0x9e90719ec722d0d480bb68bfa3f6a3260e8d2b749bb6da000000000000,0x217277f77e01580cd32788186c96066a0711c72a98d891fc000000000000,
0x72f97c62c1249eac15d7e3d3f543b60c784d1ca26d6875d24000000000000,0x192693359a4002b5a4c739d65da6cfd2ba50de4387eed9c5fe0000000000000,
0x59996c6ef58409a71b05be0bada2445eb7c017d09442e7d158e0000000000000,0x144cc291239fea2fdc1f4d0ea556c37d75a18565419728856e22c0000000000000,
0x4adb0d77335daf907bb36c2601aff0dea1c39be561dd656c0620240000000000000,0x118b5727f009f525dcfe0d58e8653c742de9d889c2efe3c5516f88700000000000000,
0x42e33c484325f6a05a8892e2f601f67aef0b898d373294604679382b00000000000000,0x10330899804331bad5ed1392f79479b1c5e4cb50335e3fef51115b9a6a00000000000000,
0x3fc8f1dc690893cfaa557d12aed89f2bfb34e08bca431bbe4f3458b001600000000000000,0xff23c771a4224f3ea955f44abb627cafecd3822f290c6ef93cd162c0058000000000000000,
0x40c815a3daacb61ee8fed306f99401a8ab21b40df96c282d48712a12c1658000000000000000,0x10b395943e6086f3f811b267cc58286d7c1eb06b9a4de25bacad2cd8d5dc2b0000000000000000,
0x45f0025cc534351d9eca1b12a7b1294a77c082c2962623dfe3152bcbff89f410000000000000000,
0x1293c0a0a461de1bde2daf30f48b0ef7c7cf22bbafe2218778519fa22fe0a4d440000000000000000,
0x501d2eb4c4e60dd82e2503831e97b08c8dad45c9667f309836e0006b6e78c6d3540000000000000000,
0x15e7fac56dd6e7c91c9e1ef5da5d7a466ebd61151206c7499f01401d6035065dc8f80000000000000000,
0x613568cc1769a48c6efda962f8fece988b685ecd7ffe1456b1958c825aeb4c402bcc80000000000000000,
0x1b5705796695b6477f3757a3d607aa1ae7355aa9cbff75b861f20f84a9922d720c518400000000000000000,
0x7cbd08f9e40b0fa6346c7fdb8082f81abee36da6b2bd89193ee066cd45aaef585833ea400000000000000000,
0x240ea4983beb32860b275cf57325dbb7bb2dbdb22faac9a14c2cddb75623692f897f01b6800000000000000000,
0xa904a38998de7cd4544883be8bc175ed3d6669333f70912415124f4b63c5fd0ed48358077800000000000000000,
0x322d608cd9620d0f0905871c917d6f026e3a673b36d56b16b6416f8a619ec7206716fe2237a000000000000000000,
0xf17a60a5d627ded85b6a9a397c2ba63bb27910ccf7e3135d4d1ae8c9f5cc1e4bf01ea704abb2000000000000000000,
0x49934972874025e5ebda7afd83d54ca63060e31e73872fe66d7e32ed88e4313b232956e36c503c000000000000000000,
0x16b473aa57bccbb1f3c86bf43baed2a748ede61665a6b7c81bc9f1b74d3e6b313fd9c1d02e6cc284000000000000000000,
0x71864253b6affa79c2ea1bc52a6a1d446ca57e6ffc4196e88af1b894823817f63f40c910e81fcc940000000000000000000,
0x23eb7afc7ccdae4086ac12c9626b9342a6605d016ed0c0bf93f67b66fd33bf94ea037f9e59720fbad40000000000000000000,
0xb816d64dff9e1d0ab231e048186752b594addca757eddbd5d64f386fd1a935db2f51ee0b8a68909d7e80000000000000000000,
0x3baf677b49e0436a77c62bb75fe97fd0df345e8a41821e46547baf4c40f9dc761057902dbddfe6e3100380000000000000000000,
0x13958df4743d961eef4d06582b789df0893d2f055d7eb1ef13b895850551fc56bd5cbb4f024d77c281412600000000000000000000,
0x680a8222a9872d84574931b466f0c70dd91509cc80b1114618c49a52ac438c8ccdfca313bc3b8c394eaa19e00000000000000000000,
0x22f387b7a4f3694a755296b29a94e2dea6ed114ab33b7bcd8c520bd7c5deb1374d32dec8a13c011b406d24b1400000000000000000000,
0xbe0c31f690eb8c84ddf1136b2889919aaba90e062e93712daafe206543eae39cb3c49b62ecb646042e517783cc00000000000000000000,
0x4154312cc1d0f84dac4adeacd5ef4a0d2b021cd22002aee7b2c75b22cf58be3dddcb956a015ea8116fec01154e2000000000000000000000,
0x16b645188f61a65300e6076a166030be93f3bc050d20eece8d274eaf1a15da23821bc6f1da79e86e0fe90c6068292000000000000000000000,
0x7fc144aa26854792e50de9b4bddd1230003b019c69d93f49d9fd1a98f2baeb07bbdc3f106cedbb6b197ee59e49e754000000000000000000000,
0x2d69b3687bb16071376bf2133f7d95771014f99299a0397f407cf8745e48718bbfc74a6ad6b8819f12101b9f44453adc000000000000000000000,
0x1051fc798c73bea8afeacafeead121b6c9c789b0af3594a9bb2ce949d1e208ce38eb9ebe652a4e952a7dc9ed3c88e12710000000000000000000000,
0x5edc8b828060c4347e84bbe9b4df93f674d7d052fa67701a8ff50bfd13f1d32eaad98ab2ac05e8c306fb25b2efdb9cb30d0000000000000000000000,
0x22d4fb39eb23880b4674bcffd06a18547ee73e7e77f1fb29c0dbfa66ed52cb8b22bbe0ed9b2a2b779c9037d7b412a389bec60000000000000000000000,
0xced093a7e422f7c2f255222ee575f075b17d030ee82cc347e91a1ec3211b988a1e3b8782c94a621631984b90bd2eab01dcb7a0000000000000000000000,
0x4d8e375ef58d1ce91adfecd1960c3a2c228ee1259710c93af769cb892c6a5933cb5652d10b7be4c852991c5646f18020b2c4dc00000000000000000000000,
0x1d62e2fafb0a77f4532ed8bb69daa20ab918234f3e3d5c3f57bf161ef9d44bcca00bb5613559f1afe74c03bcb0e1818c63bc975c00000000000000000000000,
0xb3fdae4141a01eb87d7eef7be85b2081adb3d8455d37d503f972677dba3450455447b6f366c6e85568b196e3bb65397be2e31f13800000000000000000000000,
0x459b1a633c60ebe15888169ceadb3d92262c8ca2d30c976089773e059f023b0acf97bbc020beebd9077cad5a1178253ae8bdd5048a800000000000000000000000,
0x1b30964ec395dc24069528d54bbda40d16e966ef9a70eb21b5b2943a321cdf10391745570cca9420c6ecb3b72ed2ee8b02ea2735c61a000000000000000000000000)

FIRST_100_FACTORIALS = dict(enumerate(FIRST_100_FACTORIALS))

# Helper classes
class Comparitors:
    EQUALS = 0
    LESS_THAN = 1
    GREATER_THAN = 2
    NOT_EQUALS = 3
    LESS_THAN_EQUALS = 4
    GREATER_THAN_EQUALS = 5
class Generator:
    def __init__(self, raw_generator, limit=-1, initial=[], condition=None, is_numeric_sequence=False):
        self.next_index = 0
        self.is_numeric_sequence = is_numeric_sequence
        if "__name__" in dir(raw_generator) and type(raw_generator) != Python_Generator:
            if raw_generator.__name__.startswith("FN_") or raw_generator.__name__.startswith("_lambda"):
                # User defined function
                def gen():
                    generated = initial
                    factor = len(initial)
                    for item in initial:
                        yield item
                    while True:
                        if len(generated) >= (limit + factor) and limit > 0:
                            break
                        else:
                            ret = raw_generator(generated[::-1], arity=len(generated))
                            generated.append(ret[-1])
                            yield ret[-1]
                self.gen = gen()
            else:
                def gen():
                    index = 0
                    while True:
                        yield raw_generator(index)
                        index += 1
                self.gen = gen()
        else:
            def niceify(item):
                t_item = VY_type(item)
                if t_item not in [Generator, list, Number, str]:
                    return list(item)
                return item
            self.gen = map(niceify, raw_generator)
        self.generated = []
    def __contains__(self, item):
        if self.is_numeric_sequence:
            if item in self.generated: return True
            temp = next(self)
            while temp <= item:
                temp = next(self)
            return item in self.generated
        else:
            for temp in self:
                if item == temp: return True
            return False
    def __getitem__(self, position):
        if type(position) is slice:
            ret = []
            stop = position.stop or self.__len__()
            start = position.start or 0

            if stop < 0:
                stop = self.__len__() - position.stop - 2


            if position.step and position.step < 0:
                start, stop = stop, start
                stop -= 1
                start -= 1
            # print(start, stop, position.step or 1)
            for i in range(start, stop, position.step or 1):
                ret.append(self.__getitem__(i))
                # print(self.__getitem__(i))
            return ret
        if position < 0:
            return list(self.gen)[position]
        if position < len(self.generated):
            return self.generated[position]
        while len(self.generated) < position + 1:
            try:
                self.__next__()
            except:
                position = position % len(self.generated)

        return self.generated[position]
    def __setitem__(self, position, value):
        if position >= len(self.generated):
            temp = self.__getitem__(position)
        self.generated[position] = value
    def __len__(self):
        return len(self._dereference())
    def __next__(self):
        f = next(self.gen)
        self.generated.append(f)
        return f
    def __iter__(self):
        return self
    def _filter(self, function):
        index = 0
        l = self.__len__()
        while True:
            if index == l:
                break
            obj = self.__getitem__(index)
            ret = _safe_apply(function, obj)
            if ret:
                yield obj
            index += 1
    def _reduce(self, function):
        def ensure_singleton(function, left, right):
            ret = _safe_apply(function, left, right)
            if type(ret) in [Generator, list]:
                return ret[-1]
            return ret
        return functools.reduce(lambda x, y: ensure_singleton(function, x, y), self._dereference())
    def _dereference(self):
        '''
        Only call this when it is absolutely neccesary to convert to a list.
        '''
        d = self.generated + list(self.gen)
        self.gen = iter(d[::])
        self.generated = []
        return d
    def _print(self, end="\n"):
        main = self.generated
        try:
            f = next(self)
            # If we're still going, there's stuff in main that needs printing before printing the generator
            VY_print("⟨", end="")
            for i in range(len(main)):
                VY_print(main[i], end="|"*(i >= len(main)))
            while True:
                try:
                    f = next(self)
                    VY_print("|", end="")
                    VY_print(f, end="")
                except:
                    break
            VY_print("⟩", end=end)

        except:
            VY_print(main, end=end)


    def zip_with(self, other):
        return Generator(zip(self.gen, iter(other)))
    def safe(self):
        import copy
        return copy.deepcopy(self)

class ShiftDirections:
    LEFT = 1
    RIGHT = 2

# Helper functions
def _safe_apply(function, *args):
    '''
    Applies function to args that adapts to the input style of the passed function.

    If the function is a _lambda (it's been defined within λ...;), it passes a list of arguments and length of argument list
    Otherwise, if the function is a user-defined function (starts with FN_), it simply passes the argument list
    Otherwise, unpack args and call as usual
    '''

    if function.__name__.startswith("_lambda"):
        ret = function(list(args), len(args), function)
        if len(ret): return ret[-1]
        else: return []
    elif function.__name__.startswith("FN_"):
        ret = function(list(args))[-1]
        if len(ret): return ret[-1]
        else: return []
    return function(*args)
def _mangle(value):
    byte_list = bytes(value, encoding="utf-8")
    return base64.b32encode(byte_list).decode().replace("=", "_")
def _two_argument(function, left, right):
    '''
    Used for vectorising user-defined lambas/dyads over generators
    '''
    if function.__name__.startswith("_lambda"):
        return Generator(map(lambda x: function(x, arity=2), VY_zip(left, right)))
    return Generator(map(lambda x: function(*x), VY_zip(left, right)))
def add(lhs, rhs):
    '''
    Returns lhs + rhs. Check command docs for type cohesion.
    '''
    types = VY_type(lhs), VY_type(rhs)
    return {
        (Number, Number): lambda: lhs + rhs,
        (str, str): lambda: lhs + rhs,
        (str, Number): lambda: str(lhs) + str(rhs),
        (Number, str): lambda: str(lhs) + str(rhs),
        (list, types[1]): lambda: [add(item, rhs) for item in lhs],
        (types[0], list): lambda: [add(lhs, item) for item in rhs],
        (list, list): lambda: list(map(lambda x: add(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(add, lhs, rhs),
        (Generator, list): lambda: _two_argument(add, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(add, lhs, rhs)
    }.get(types, lambda: vectorise(add, lhs, rhs))()
def all_combinations(vector):
    ret = []
    for i in range(len(vector) + 1):
        ret = join(ret, combinations_replace_generate(vector, i))
    return ret
def all_prime_factors(item):
    if VY_type(item) == Number:
        m = sympy.ntheory.factorint(int(item))
        out = []
        for key in sorted(m.keys()):
            out += [key] * m[key]
        return out
    elif VY_type(item) is str:
        return item.title()
    return vectorise(all_prime_factors, item)
def assigned(vector, index, item):
    if type(vector) is str:
        vector = list(vector)
        vector[index] = item
        return "".join([str(x) for x in vector])
    else:
        temp = deref(vector, False)
        temp[index] = item
        return temp
def bifuricate(item):
    t_item = VY_type(item)
    if t_item in (Number, list, str):
        return [item, reverse(item)]
    else:
        g = item._dereference()
        return [g, reverse(g)]
def bit_and(lhs, rhs):
    types = (VY_type(lhs), VY_type(rhs))
    return {
        (Number, Number): lambda: lhs & rhs,
        (Number, str): lambda: rhs.center(lhs),
        (str, Number): lambda: lhs.center(rhs),
        (str, str): lambda: lhs.center(len(rhs) - len(lhs)),
        (types[0], list): lambda: [bit_and(lhs, item) for item in rhs],
        (list, types[1]): lambda: [bit_and(item, rhs) for item in lhs],
        (list, list): lambda: list(map(lambda x: bit_and(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(bit_and, lhs, rhs),
        (Generator, list): lambda: _two_argument(bit_and, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(bit_and, lhs, rhs)
    }.get(types, lambda: vectorise(bit_and, lhs, rhs))()
def bit_or(lhs, rhs):
    types = (VY_type(lhs), VY_type(rhs))
    if types == (str, str):
        suffixes = {lhs[-i:] for i in range(1, len(lhs) + 1)}
        prefixes = {rhs[:i] for i in range(1, len(rhs) + 1)}
        common = suffixes & prefixes
        if len(common) == 0:
            return lhs + rhs
        common = common.pop()
        return lhs[:-len(common)] + common + rhs[len(common):]
    return {
        (Number, Number): lambda: lhs | rhs,
        (Number, str): lambda: lhs[:rhs] + lhs[rhs + 1:],
        (str, Number): lambda:  rhs[:lhs] + rhs[lhs + 1:],
        (types[0], list): lambda: [bit_or(lhs, item) for item in rhs],
        (list, types[1]): lambda: [bit_or(item, rhs) for item in lhs],
        (list, list): lambda: list(map(lambda x: bit_or(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(bit_or, lhs, rhs),
        (Generator, list): lambda: _two_argument(bit_or, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(bit_or, lhs, rhs)
    }.get(types, lambda: vectorise(bit_or, lhs, rhs))()
def bit_not(item):
    return {
        str: lambda: int(any(map(lambda x: x.isupper(), item))),
        Number: lambda: ~item
    }.get(VY_type(item), lambda: vectorise(bit_not, item))()
def bit_xor(lhs, rhs):
    types = (VY_type(lhs), VY_type(rhs))
    return {
        (Number, Number): lambda: lhs ^ rhs,
        (Number, str): lambda: (" " * lhs) + rhs,
        (str, Number): lambda: lhs + (" " * rhs),
        (str, str): lambda: levenshtein_distance(lhs, rhs),
        (types[0], list): lambda: [bit_xor(lhs, item) for item in rhs],
        (list, types[1]): lambda: [bit_xor(item, rhs) for item in lhs],
        (list, list): lambda: list(map(lambda x: bit_xor(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(bit_xor, lhs, rhs),
        (Generator, list): lambda: _two_argument(bit_xor, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(bit_xor, lhs, rhs)
    }.get(types, lambda: vectorise(bit_xor, lhs, rhs))()
def cartesian_product(lhs, rhs):
    if Function not in (VY_type(lhs), VY_type(rhs)):
        lhs, rhs = iterable(lhs), iterable(rhs)
        if (VY_type(lhs), VY_type(rhs)) in ((Number, Number), (Number, str), (str, Number), (str, str)):
            return Generator(map(first_n, itertools.product(iterable(lhs), iterable(rhs))))
        return Generator(itertools.product(iterable(lhs), iterable(rhs)))
    
    if VY_type(lhs) is Function:
        fn, init = lhs, rhs
    else:
        fn, init = rhs, lhs
    def gen():
        prev = None
        curr = init
        while prev != curr:
            prev = deref(curr)
            curr = fn([curr])[-1]
        yield curr
    return Generator(gen())
def ceiling(item):
    return {
        Number: lambda: math.ceil(item),
        str: lambda: item.split(" ")
    }.get(VY_type(item), lambda: vectorise(ceiling, item))()
def centre(vector):
    vector = deref(iterable(vector), True)
    focal = max(map(len, vector))
    def gen():
        for item in vector:
            yield item.center(focal)

    return Generator(gen())
def chrord(item):
    t_item = VY_type(item)
    if t_item is str and len(item) == 1:
        return ord(item)
    elif t_item == Number:
        return chr(int(item))
    else:
        return Generator(map(chrord, item))
def closest_prime(item):
    up, down = next_prime(item), prev_prime(item)
    if abs(item - down) < abs(item - up): return down
    return up
def compare(lhs, rhs, mode):
    op = ["==", "<", ">", "!=", "<=", ">="][mode]

    types = tuple(map(VY_type, [lhs, rhs]))
    boolean =  {
        types: lambda lhs, rhs: eval(f"lhs {op} rhs"),
        (Number, str): lambda lhs, rhs: eval(f"str(lhs) {op} rhs"),
        (str, Number): lambda lhs, rhs: eval(f"lhs {op} str(rhs)"),
        (types[0], list): lambda *x: [compare(lhs, item, mode) for item in rhs],
        (list, types[1]): lambda *x : [compare(item, rhs, mode) for item in lhs],
        (Generator, types[1]): lambda *y: vectorise(lambda x: compare(x, rhs, mode), lhs),
        (types[0], Generator): lambda *y: vectorise(lambda x: compare(lhs, x, mode), rhs),
        (list, list): lambda *y: list(map(lambda x: compare(*x, mode), VY_zip(lhs, rhs))),
        (list, Generator): lambda *y: Generator(map(lambda x: compare(*x, mode), VY_zip(lhs, rhs))),
        (Generator, list): lambda *y: Generator(map(lambda x: compare(*x, mode), VY_zip(lhs, rhs))),
        (Generator, Generator): lambda *y: Generator(map(lambda x: compare(*x, mode), VY_zip(lhs, rhs))),
    }[types](lhs, rhs)
    if type(boolean) is bool:
        return int(boolean)
    else:
        return boolean
def complement(item):
    return {
        Number: lambda: 1 - item,
        str: lambda: item.split(",")
    }.get(VY_type(item), lambda: vectorise(complement, item))()
def combinations_replace_generate(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)
    if Function not in types:
        ret = {
            (Number, types[1]): lambda: Generator(itertools.product(iterable(rhs), repeat=lhs)),
            (types[0], Number): lambda: Generator(itertools.product(iterable(lhs), repeat=rhs))
        }.get(types, lambda: -1)()
        if ret != -1: return ret
        out = "" if type(lhs) is str else []
        for item in lhs:
            if item in rhs:
                if type(lhs) is str: out += item
                else: out.append(item)
        return out
    else:
        if VY_type(lhs) is Function:
            fn, init = lhs, rhs
        else:
            fn, init = rhs, lhs
        def gen():
            prev = None
            curr = init
            while prev != curr:
                yield curr
                prev = deref(curr)
                curr = fn([curr])[-1]
        return Generator(gen())
def const_divisibility(item, n, string_overload):
    return {
        Number: lambda: int(item % n == 0),
        str: lambda: int(string_overload(item))
    }.get(VY_type(item), lambda: vectorise(const_divisibility, item, n, string_overload))()
def counts(vector):
    ret = []
    vector = iterable(vector)
    for item in set(vector):
        ret.append([item, vector.count(item)])
    return ret
def cumulative_sum(vector):
    ret = []
    vector = iterable(vector)
    # if VY_type(vector) is Generator: vector = vector._dereference()
    for i in range(len(vector)):
        ret.append(summate(vector[:i + 1]))
    return ret
def decimalify(vector):
    if VY_type(vector) == Number:
        return iterable(vector)
    elif VY_type(vector) is str:
        return list(vector)
    else:
        return functools.reduce(lambda x, y: divide(x, y), vector)
def deltas(vector):
        ret = []
        vector = iterable(vector)
        for i in range(len(vector) - 1):
            ret.append(subtract(vector[i], vector[i + 1]))
        return ret
def deref(item, generator_to_list=True):
    if VY_type(item) is Generator:return [item.safe, item._dereference][generator_to_list]()
    if type(item) not in [int, float, str]: return list(map(deref, item))
    return item
def dictionary_compress(item):
    item = split_on_words(VY_str(item))
    out = ""

    for word in item:
        temp = words.word_index(word)
        if temp == -1:
            out += word
        else:
            out += temp
    return "`" + out + "`"
def diagonals(vector):
    # Getting real heavy Mornington Crescent vibes from this
    vector = numpy.asarray(vector)
    diag_num = 0
    diagonal = numpy.diag(vector)
    # postive diags first
    while len(diagonal):
        yield vectorise(lambda x: x.item(), list(diagonal))
        diag_num += 1
        diagonal = numpy.diag(vector, k=diag_num)
    
    diag_num = -1
    diagonal = numpy.diag(vector, k=diag_num)
    # now the other diagonals
    while len(diagonal):
        yield vectorise(lambda x: x.item(), list(diagonal))
        diag_num -= 1
        diagonal = numpy.diag(vector, k=diag_num)
def distance_between(lhs, rhs):
    inner = Generator(map(lambda x: exponate(subtract(x[0], x[1]), 2), VY_zip(lhs, rhs)))
    inner = summate(inner)
    return exponate(inner, 0.5)
def distribute(vector, value):
    types = VY_type(vector), VY_type(value)
    if types == (Number, Number):
        return abs(vector - value)
    vector = iterable(vector)
    if VY_type(vector) is Generator:
        vector = vector._dereference()
    remaining = value
    index = 0
    while remaining > 0:
        vector[index % len(vector)] += 1
        index += 1
        remaining -= 1

    return vector
def divide(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)
    def handle_numbers(lhs, rhs):
        if rhs == 0: return 0
        normal, int_div = lhs / rhs, lhs // rhs
        return [normal, int_div][normal == int_div]
    return {
        (Number, Number): lambda: handle_numbers(lhs, rhs),
        (str, str): lambda: split(lhs, rhs),
        (str, Number): lambda: wrap(lhs, len(lhs) // rhs),
        (Number, str): lambda: wrap(rhs, len(rhs) // lhs),
        (list, types[1]): lambda: [divide(item, rhs) for item in lhs],
        (types[0], list): lambda: [divide(lhs, item) for item in rhs],
        (list, list): lambda: list(map(lambda x: divide(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(divide, lhs, rhs),
        (Generator, list): lambda: _two_argument(divide, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(divide, lhs, rhs)
    }.get(types, lambda: vectorise(divide, lhs, rhs))()
def divisors_of(item):
    t_item = VY_type(item)
    if t_item in [list, Generator]:
        return Generator(prefixes(item))

    divisors = []
    if t_item == str:
        def gen():
            s = list(item)
            i = itertools.chain.from_iterable(\
                itertools.combinations(s, r) for r in range(1,len(s)+1))

            for sub in i:
                sub = "".join(sub)
                if len(item.split(sub)) == 2:
                    yield sub

        return Generator(gen())

    for value in VY_range(item, 1, 1):
        if modulo(item, value) == 0:
            divisors.append(value)

    return divisors
def exponate(lhs, rhs):
    types = (VY_type(lhs), VY_type(rhs))

    if types == (str, str):
        pobj = regex.compile(lhs)
        mobj = pobj.search(rhs)
        return list(mobj.span()) if mobj else []

    if types == (str, Number):
        factor = rhs
        if 0 < rhs < 1:
            factor = int(1 / rhs)
        return lhs[::factor]
    return {
        (Number, Number): lambda: lhs ** rhs,
        (types[0], list): lambda: [exponate(lhs, item) for item in rhs],
        (list, types[1]): lambda: [exponate(item, rhs) for item in lhs],
        (list, list): lambda: list(map(lambda x: exponate(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(exponate, lhs, rhs),
        (Generator, list): lambda: _two_argument(exponate, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(exponate, lhs, rhs)
    }.get(types, lambda: vectorise(exponate, lhs, rhs))()
def factorial(item):
    t_item = VY_type(item)
    if t_item == Number:
        if item in FIRST_100_FACTORIALS:
            return FIRST_100_FACTORIALS[item]
        else:
            FIRST_100_FACTORIALS[item] = math.factorial(item)
        return  FIRST_100_FACTORIALS[item]
    elif t_item == str:
        return sentence_case(item)
    else:
        return vectorise(factorial, item)
def factorials():
    # Different to factorial because this is a list of all factorials
    for i in range(1,101):
        yield FIRST_100_FACTORIALS[i]
    
    temp = FIRST_100_FACTORIALS[100]
    n = 101

    while True:
        temp *= n
        FIRST_100_FACTORIALS[n] = temp
        n += 1
        yield temp
def fibonacci():
    # A generator of all the fibonacci numbers
    # Pro-tip: wrap in a generator before pushing to stack
    
    yield 0
    yield 1
    
    memory = [0, 1]
    while True:
        temp = memory[-1] + memory[-2]
        memory.append(temp)
        yield temp
def find(haystack, needle, start=0):
    if type(needle) is Function:
        return indexes_where(haystack, needle)
    # It looks like something from 2001
    index = 0
    haystack = iterable(haystack)
    if type(haystack) is str:
        needle = str(needle)
    if type(start) is int or (type(start) is str and start.isnumeric()):
        index = start
    while index < len(haystack):
        if haystack[index] == needle:
            return index
        index += 1
    return -1
def first_n(func, n=None):
    if Function not in (type(func), type(n)):
        if n:
            return iterable(func)[n:]
        
        ret = "".join([VY_str(n) for n in iterable(func)])
        return VY_eval(ret)
    ret = []
    current_index = 0
    n = n or 1
    if isinstance(n, Function):
        call, limit = n, func
    else:
        call, limit = func, n
    while len(ret) < limit:
        result = call([current_index])[-1]
        if result: ret.append(current_index)
        current_index += 1

    return ret
def flatten(item):
    '''
    Returns a deep-flattened (all sublists expanded) version of the input
    '''
    t_item = VY_type(item)
    if t_item is Generator:
        return Generator(functools.reduce(list.__add__, item))
    else:
        ret = []
        for x in item:
            if type(x) is list:
                ret += flatten(x)
            else:
                ret.append(x)
        return ret
def floor(item):
    return {
        Number: lambda: math.floor(item),
        str: lambda: int("".join([l for l in item if l in "0123456789"]))
    }.get(VY_type(item), lambda: vectorise(floor, item))()
def format_string(value, items):
    ret = ""
    index = 0
    f_index = 0

    while index < len(value):
        if value[index] == "\\":
            ret += "\\" + value[index + 1]
            index += 1
        elif value[index] == "%":
            #print(f_index, f_index % len(items))
            ret += str(items[f_index % len(items)])
            f_index += 1
        else:
            ret += value[index]
        index += 1
    return ret
def fractionify(item):
    import re
    if VY_type(item) == Number:
        from fractions import Fraction
        from decimal import Decimal
        frac = Fraction(item).limit_denominator()
        return [frac.numerator, frac.denominator]
    elif type(item) is str:
        if re.match(r"\-?\d+(\.\d+)?", item): return fractionify(eval(item))
        else: return item
    else:
        return vectorise(fractionify, item)
def function_call(fn, vector):
    if type(fn) is Function:
        return fn(vector, self=fn)
    else:
        return [{
            Number: lambda: len(prime_factors(fn)),
            str: lambda: exec(VY_compile(fn))
        }.get(VY_type(fn), lambda: vectorised_not(fn))()]
def gcd(lhs, rhs=None):
    if rhs:
        return {
            (Number, Number): lambda: math.gcd(int(lhs), int(rhs)),
            (Number, str): lambda: max(set(divisors_of(str(lhs))) & set(divisors_of(rhs)), key=lambda x: len(x)),
            (str, Number): lambda: max(set(divisors_of(lhs)) & set(divisors_of(str(rhs))), key=lambda x: len(x)),
            (str, str): lambda: max(set(divisors_of(lhs)) & set(divisors_of(rhs)), key=lambda x: len(x)),
        }.get((VY_type(lhs), VY_type(rhs)), lambda: vectorise(gcd, lhs, rhs))()

    else:
        # I can't use VY_reduce because ugh reasons
        lhs = deref(lhs, True)
        return int(numpy.gcd.reduce(lhs))   
def get_input(predefined_level=None):
    global input_values

    level = input_level
    if predefined_level is not None:
        level = predefined_level

    if level in input_values:
        source, index = input_values[level]
    else:
        source, index = [], -1
    if source:
        ret = source[index % len(source)]
        input_values[level][1] += 1

        if keg_mode and type(ret) is str:
            return [ord(c) for c in ret]
        return ret
    else:
        try:
            temp = VY_eval(input())
            if keg_mode and type(temp) is str:
                return [ord(c) for c in temp]
            return temp
        except:
            return 0
def graded(item):
    return {
        Number: lambda: item + 2,
        str: lambda: item.upper(),

    }.get(VY_type(item), lambda: Generator(map(lambda x: x[0], sorted(enumerate(item), key=lambda x: x[-1]))))()
def graded_down(item):
       return {
        Number: lambda: item - 2,
        str: lambda: item.lower(),

    }.get(VY_type(item), lambda: reverse(Generator(map(lambda x: x[0], sorted(enumerate(item), key=lambda x: x[-1])))))()
def group_consecutive(vector):
    ret = []
    temp = [vector[0]]
    last = vector[0]
    for item in vector[1:]:
        if item == last:
            temp.append(item)
        else:
            ret.append(temp)
            temp = [item]
            last = item

    if len(ret) == 0 or temp != ret[-1]:
        ret.append(temp)

    return ret
def halve(item):
    return {
        Number: lambda: divide(item, 2),
        str: lambda: wrap(item, ceiling(len(item) / 2))
    }.get(VY_type(item), lambda: vectorise(halve, item))()
def inclusive_range(lhs, rhs):
    types = (VY_type(lhs), VY_type(rhs))
    if Function in types:
        if types[0] is Function:
            func, vector = lhs, rhs
        else:
            func, vector = rhs, lhs
        
        def gen():
            for index, item in enumerate(vector):
                if (index + 1) % 2:
                    yield item
                else:
                    yield func([item])[-1]
        
        return Generator(gen())
    if types != (Number, Number):
        lhs, rhs = VY_str(lhs), VY_str(rhs)
        pobj = regex.compile(rhs)
        return pobj.split(lhs)

    if lhs < rhs:
        return Generator(range(int(lhs), int(rhs) + 1))
    else:
        return Generator(range(int(lhs), int(rhs) - 1, -1))
def index(vector, index):
    if VY_type(index) == Number:
        if VY_type(vector) is Generator:
            return vector[int(index)]
        return vector[int(index) % len(vector)]
    elif VY_type(index) in (list, Generator):
        return vector[slice(*index)]
    else:
        return [vector, index, join(vector, index)]
def indexed_into(vector, indexes):
    ret = []
    for ind in indexes:
        ret.append(vector[ind % len(vector)])
    return ret
def indexes_where(fn, vector):
    ret = []
    for i in range(len(vector)):
        if fn([vector[i]])[-1]:
            ret.append(i)
    return ret
def infinite_replace(haystack, needle, replacement):
    import copy
    loop = True
    prev = copy.deepcopy(haystack)
    while loop: # I intentionally used a post-test loop here to avoid making more calls to replace than neccesary
        haystack = replace(haystack, needle, replacement)
        loop = haystack != prev
        prev = copy.deepcopy(haystack)
    return haystack
def inserted(vector, item, index):
    temp = deref(iterable(vector), False)
    t_vector = type(temp)
    if t_vector is list:
        temp.insert(index, item)
        return temp
    return {
        str: lambda: temp[:index] + str(item) + temp[index:],
    }.get(t_vector, lambda: inserted(temp._dereference(), item, index))()
def integer_divide(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)
    return {
        (Number, Number): lambda: lhs // rhs,
        (Number, str): lambda: divide(lhs, rhs)[0],
        (str, Number): lambda: divide(lhs, rhs)[0],
        (Function, types[1]): lambda: VY_reduce(lhs, reverse(rhs))[0],
        (types[0], Function): lambda: VY_reduce(rhs, reverse(lhs))[0]
    }.get(types, lambda: vectorise(integer_divide, lhs, rhs))()
def integer_list(value):
    charmap = dict(zip("etaoinshrd", "0123456789"))
    ret = []
    for c in value.split():
        temp = ""
        for m in c:
            temp += charmap[m]
        ret.append(int(temp))
    return ret
def interleave(lhs, rhs):
    ret = []
    for i in range(min(len(lhs), len(rhs))):
        ret.append(lhs[i])
        ret.append(rhs[i])
    if len(lhs) != len(rhs):
        if len(lhs) < len(rhs):
            # The rhs is longer
            ret += list(rhs[i + 1:])
        else:
            ret += list(lhs[i + 1:])
    if type(lhs) is str and type(rhs) is str: return "".join(ret)
    return ret
def is_divisble(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)
    return {
        (Number, Number): lambda: int(modulo(lhs, rhs) == 0 and rhs != 0),
        (str, str): lambda: (lhs, ) * len(rhs),
        (str, Number): lambda: (lhs, ) * rhs,
        (Number, str): lambda: (rhs, ) * lhs
    }.get(types, lambda: vectorise(is_divisble, lhs, rhs))()
def is_empty(item):
    return {
        Number: lambda: item % 3,
        str: lambda: int(item == "")
    }.get(VY_type(item), lambda: vectorise(is_empty, item))()
def is_prime(n):
    if type(n) is str:
        if n.upper() == n.lower(): return -1
        else: return int(n.upper() == n)
    if VY_type(n) in [list, Generator]: return vectorise(is_prime, n)
    return sympy.ntheory.isprime(n)
def is_square(n):
    if type(n) in (float, str): return 0
    elif isinstance(n, int): return int(any([exponate(y, 2) == n for y in range(1, math.ceil(n / 2) + 1)])) or int(n == 0)
    else: return vectorise(is_square, n)
def iterable(item, t=None):
    t = t or number_iterable
    if VY_type(item) == Number:
        if t is list:
            return [int(let) if let not in "-." else let for let in str(item)]
        if t is range:
            return Generator(range(MAP_START, int(item) + MAP_OFFSET))
        return t(item)
    else:
        return item
def iterable_shift(vector, direction, times=1):
    vector = deref(iterable(vector))
    t_vector = type(vector)
    for _ in range(times):
        if direction == ShiftDirections.LEFT:
            if t_vector is list:
                # [1, 2, 3] -> [2, 3, 1]
                vector = vector[::-1]
                temp = pop(vector)
                vector = vector[::-1]
                vector.append(temp)
            else:
                # abc -> bca
                vector = join(vector[1:], vector[0]) 
        elif direction == ShiftDirections.RIGHT:
            if t_vector is list:
                # [1, 2, 3] -> [3, 1, 2]
                temp = pop(vector)
                vector.insert(0, temp)
            else:
                # abc -> cab
                vector = join(vector[-1], vector[:-1]) 
    
    return vector
def join(lhs, rhs):
    types = tuple(map(VY_type, [lhs, rhs]))
    return {
        (types[0], types[1]): lambda: str(lhs) + str(rhs),
        (Number, Number): lambda: VY_eval(str(lhs) + str(rhs)),
        (types[0], list): lambda: [lhs] + rhs,
        (list, types[1]): lambda: lhs + [rhs],
        (types[0], Generator): lambda: [lhs] + rhs._dereference(),
        (Generator, types[1]): lambda: lhs._dereference() + [rhs],
        (list, list): lambda: lhs + rhs,
        (list, Generator): lambda: lhs + rhs._dereference(),
        (Generator, list): lambda: lhs._dereference() + rhs,
        (Generator, Generator): lambda: lhs._dereference() + rhs._dereference()
    }[types]()
def levenshtein_distance(s1, s2):
    # https://stackoverflow.com/a/32558749
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]
def log(lhs, rhs):
    types = (VY_type(lhs), VY_type(rhs))
    if types == (str, str):
        ret = ""
        for i in range(min(len(lhs), len(rhs))):
            if rhs[i].isupper():
                ret += lhs[i].upper()
            elif rhs[i].islower():
                ret += lhs[i].lower()
            else:
                ret += lhs[i]

        if len(lhs) > len(rhs):
            ret += lhs[i + 1:]

        return ret

    return {
        (Number, Number): lambda: math.log(lhs, rhs),
        (str, Number): lambda: "".join([c * rhs for c in lhs]),
        (Number, str): lambda: "".join([c * lhs for c in rhs]),
        (list, list): lambda: mold(lhs, rhs),
        (list, Generator): lambda: mold(lhs, list(rhs)),
        (Generator, list): lambda: mold(list(lhs), rhs),
        (Generator, Generator): lambda: mold(list(lhs), list(rhs)) #There's a chance molding raw generators won't work
    }.get(types, lambda: vectorise(log, lhs, rhs))()
def lshift(lhs, rhs):
    types = (VY_type(lhs), VY_type(rhs))
    return {
        (Number, Number): lambda: lhs << rhs,
        (Number, str): lambda: rhs.ljust(lhs),
        (str, Number): lambda: lhs.ljust(rhs),
        (str, str): lambda: lhs.ljust(len(rhs) - len(lhs)),
        (types[0], list): lambda: [lshift(lhs, item) for item in rhs],
        (list, types[1]): lambda: [lshift(item, rhs) for item in lhs],
        (list, list): lambda: list(map(lambda x:lshift(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(lshift, lhs, rhs),
        (Generator, list): lambda: _two_argument(lshift, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(lshift, lhs, rhs)
    }.get(types, lambda: vectorise(lshift, lhs, rhs))()
def map_at(function, vector, indexes):
    def gen():
        for pos, element in enumerate(vector):
            if pos in indexes:
                yield function([element])[-1]
            else:
                yield element
    return Generator(gen())
def map_every_n(vector, function, index):
    def gen():
        for pos, element in enumerate(vector):
            if (pos + 1) % index:
                yield element
            else:
                yield function([element])[-1]
    return Generator(gen())
def modulo(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)

    if types[1] is Number and rhs == 0: return 0
    return {
        (Number, Number): lambda: lhs % rhs,
        (str, str): lambda: format_string(lhs, [rhs]),
        (str, Number): lambda: divide(lhs, rhs)[-1],
        (Number, str): lambda: divide(lhs, rhs)[-1],
        (list, types[1]): lambda: [modulo(item, rhs) for item in lhs],
        (types[0], list): lambda: [modulo(lhs, item) for item in rhs],
        (str, list): lambda: format_string(lhs, rhs),
        (list, list): lambda: list(map(lambda x: modulo(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(modulo, lhs, rhs),
        (Generator, list): lambda: _two_argument(modulo, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(modulo, lhs, rhs)
    }.get(types, lambda: vectorise(modulo, lhs, rhs))()
def mold(content, shape):
    temp = deref(shape, False)
    #https://github.com/DennisMitchell/jellylanguage/blob/70c9fd93ab009c05dc396f8cc091f72b212fb188/jelly/interpreter.py#L578
    for index in range(len(temp)):
        if type(temp[index]) == list:
            mold(content, temp[index])
        else:
            item = content.pop(0)
            temp[index] = item
            content.append(item)
    return temp
def multiply(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)
    if types == (Function, Number):
        lhs.stored_arity = rhs
        return lhs
    elif types == (Number, Function):
        rhs.stored_arity = lhs
        return rhs
    return {
        (Number, Number): lambda: lhs * rhs,
        (str, str): lambda: [x + rhs for x in lhs],
        (str, Number): lambda: lhs * rhs,
        (Number, str): lambda: lhs * rhs,
    }.get(types, lambda: vectorise(multiply, lhs, rhs))()
def ncr(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)
    return {
        (Number, Number): lambda: unsympy(sympy.functions.combinatorial.numbers.nC(int(lhs), int(rhs))),
        (str, Number): lambda: [random.choice(lhs) for c in range(rhs)],
        (Number, str): lambda: [random.choice(rhs) for c in range(lhs)],
        (str, str): lambda: int(set(lhs) == set(rhs))
    }.get(types, lambda: vectorise(ncr, lhs, rhs))()
def negate(item):
    return {
        Number: lambda: -item,
        str: lambda: item.swapcase()
    }.get(VY_type(item), lambda: vectorise(negate, item))()
def next_prime(item):
    if not isinstance(item, int):
        return item
    
    factor = 1
    while not is_prime(item + factor):
        factor += 1
    
    return item + factor
def nth_prime(item):
    t_item = VY_type(item)
    return {
        Number: lambda: sympy.ntheory.prime(int(item) + 1),
        str: lambda: Generator(substrings(item))
    }.get(t_item, lambda: vectorise(nth_prime, item))()
def nwise_pair(lhs, rhs):
    if VY_type(rhs) != Number:
        return len(iterable(lhs)) == len(rhs)
    iters = itertools.tee(iterable(lhs), rhs)
    for i in range(len(iters)):
        for j in range(i):
            next(iters[i], None)

    return Generator(zip(*iters))
def nub_sieve(vector):
    def gen():
        occurances = {}
        for item in vector:
            yield int(item not in occurances)
            if item in occurances: occurances[item] += 1
            else: occurances[item] = 1
    return Generator(gen())
def one_argument_tail_index(vector, index, start):
    types = (VY_type(vector), VY_type(index))
    if Number not in types:
        lhs, rhs = VY_str(vector), VY_str(index)
        pobj = regex.compile(lhs)
        if start == 0:
            return pobj.findall(rhs)
        else:
            return pobj.match(rhs).groups()
    return {
        (Number, Number): lambda: iterable(vector)[start:index],
        (Number, types[1]): lambda: index[start:vector],
        (types[0], Number): lambda: vector[start:index]
    }[types]()
def order(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)
    if types == (Number, Number):
        if rhs == 0 or abs(rhs) == 1: return "Infinite"
        elif lhs == 0: return 0
        temp, remainder = lhs, 0
        count = 0
        while True:
            temp, remainder = divmod(temp, rhs)
            if remainder: break
            count += 1
        return count
    else:
        return infinite_replace(iterable(lhs, str), iterable(rhs, str), "")
def orderless_range(lhs, rhs, lift_factor=0):
    types = (VY_type(lhs), VY_type(rhs))
    if types == (Number, Number):
        if lhs < rhs:
            return Generator(range(lhs, rhs + lift_factor))
        else:
            return Generator(range(lhs, rhs + lift_factor, -1))
    elif Function in types:
        if types[0] is Function:
            func, vector = lhs, iterable(rhs, range)
        else:
            func, vector = rhs, iterable(lhs, range)

        def gen():
            for pre in prefixes(vector):
                yield VY_reduce(func, pre)[-1]
        
        return Generator(gen())
    else:
        lhs, rhs = VY_str(lhs), VY_str(rhs)
        pobj = regex.compile(lhs)
        mobj = pobj.search(rhs)
        return int(bool(mobj))
def overloaded_iterable_shift(lhs, rhs, direction):
    if type(rhs) is not int:
        return [lhs, iterable_shift(rhs, direction)]
    else:
        return [iterable_shift(lhs, direction, rhs)]  
def palindromise(item):
    # This is different to m or bifuricate and join because it doesn't have two duplicate in the middle
    return join(item, reverse(item)[1:])
def partition(item, I=1):
    # https://stackoverflow.com/a/44209393/9363594
    yield [item]
    for i in range(I, item//2 + 1):
        for p in partition(item-i, i):
            yield [i] + p
def permutations(vector):
    t_vector = VY_type(vector)
    vector = itertools.permutations(vector)

    if t_vector is str:
        return Generator(map(lambda x: "".join(x), vector))
    return Generator(vector)
def polynomial(vector):
    t_vector = VY_type(vector)
    if t_vector is Generator:
        vector = vector._dereference()
    return numpy.roots(vector).tolist()
def pop(vector, num=1, wrap=False):
    ret = []

    for _ in range(num):
        if vector:
            ret.append(vector.pop())
        else:
            x = get_input()
            ret.append(x)

    if retain_items:
        vector += ret[::-1]
    
    if num == 1 and not wrap:
        return ret[0]
    
    if reverse_args:
        return ret[::-1]
    return ret
def powerset(vector):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    if type(vector) is Generator:
        vector = vector._dereference()
    elif type(vector) is str:
        vector = list(vector)
    return Generator(itertools.chain.from_iterable(itertools.combinations(vector, r) for r in range(len(vector)+1)))
def prefixes(vector):
    for i in range(len(iterable(vector))):
        yield iterable(vector)[0:i+1]
def prime_factors(item):
    t_item = VY_type(item)
    return {
        Number: lambda: sympy.ntheory.primefactors(int(item)),
        str: lambda: item + item[0]
    }.get(t_item, lambda: vectorise(prime_factors, item))()
def prepend(vector, item):
    vector = iterable(vector, range)
    t_vector = type(vector)
    return {
    list: lambda: [item] + vector,
    str: lambda: str(item) + vector,
    range: lambda: [item] + list(vector)
    }.get(t_vector, lambda: prepend(vector._dereference(), item))()
def prev_prime(item):
    if not isinstance(item, int):
        return item
    if item <= 2: return 0
    factor = 1
    while not is_prime(item - factor) and item - factor >= 2:
        factor += 1
    
    return item - factor
def product(vector):
    if type(vector) is Generator:
        return vector._reduce(multiply)
    if not vector: return 0
    ret = vector[0]
    for item in vector[1:]:
        ret = multiply(ret, item)
    return ret
def rand_between(lhs, rhs):
    if type(lhs) is int and type(rhs) is int:
        return random.randint(lhs, rhs)

    else:
        return random.choice([lhs, rhs])
def regex_replace(source, pattern, replacent):
    if type(replacent) is not Function: 
        return regex.sub(pattern, VY_str(replacent), source)
    
    parts = regex.split("(" + pattern + ")", source)
    out = ""
    switch = 1
    for item in parts:
        
        if switch % 2:
            out += item
        else:
            out += replacent([item])[-1]
        switch += 1
    
    return out
def remove(vector, item):
    return {
        str: lambda: vector.replace(str(item), ""),
        Number: lambda: str(vector).replace(str(item), ""),
        list: lambda: Generator(filter(lambda x: x != item, vector)),
        Generator: lambda: remove(vector._dereference(), item)
    }[VY_type(vector)]()
def repeat(vector, times, extra=None):
    vector = iterable(vector)
    t_vector = VY_type(vector)
    if t_vector is Function and VY_type(times) is Function:
        def gen():
            item = extra
            while vector([item])[-1]:
                item = times([item])[-1]
                yield item
        return Generator(gen())
    
    elif times < 0:
        if t_vector is str: return vector[::-1] * times
        return Generator(itertools.repeat(reversed(vector), times))
    else:
        if t_vector is str: return vector * times
        return Generator(itertools.repeat(vector, times))
def repeat_no_collect(predicate, modifier, value):
    def gen():
        item = value
        while predicate([item])[-1]:
            item = modifier([item])[-1]
        yield item
    return gen()
def replace(haystack, needle, replacement):
    t_haystack = VY_type(haystack)
    if t_haystack is list:
        return [replacement if value == needle else value for value in haystack]
    elif t_haystack is Generator:
        return replace(haystack._dereference(), needle, replacement) # Not sure how to do replacement on generators yet
    else:
        return str(haystack).replace(str(needle), str(replacement))
def reverse(vector):
    if type(vector) in [float, int]:
        s_vector = str(vector)
        if vector < 0:
            return -type(vector)(s_vector[1:][::-1])
        else:
            return type(vector)(s_vector[::-1])
    return vector[::-1]
def rshift(lhs, rhs):
    types = (VY_type(lhs), VY_type(rhs))
    return {
        (Number, Number): lambda: lhs >> rhs,
        (Number, str): lambda: rhs.rjust(lhs),
        (str, Number): lambda: lhs.rjust(rhs),
        (str, str): lambda: lhs.rjust(len(lhs) - len(rhs)),
        (types[0], list): lambda: [rshift(lhs, item) for item in rhs],
        (list, types[1]): lambda: [rshift(item, rhs) for item in lhs],
        (list, list): lambda: list(map(lambda x:rshift(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(rshift, lhs, rhs),
        (Generator, list): lambda: _two_argument(rshift, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(rshift, lhs, rhs)
    }.get(types, lambda: vectorise(rshift, lhs, rhs))()
def run_length_decode(vector):
    ret = ""
    for item in vector:
        ret += item[0] * item[1]
    return ret
def run_length_encode(item):
    item = group_consecutive(iterable(item))
    return Generator(map(lambda x: [x[0], len(x)], item))
def sentence_case(item):
    ret = ""
    capitalise = True
    for char in item:
        ret += (lambda: char.lower(), lambda: char.upper())[capitalise]()
        if capitalise and char != " ": capitalise = False
        capitalise = capitalise or char in "!?."
    return ret
def set_caret(lhs, rhs):
    # Why make my own function instead of using standard ^? Because numbers and strings. that's why.
    types = VY_type(lhs), VY_type(rhs)
    new_lhs, new_rhs = {
        (Number, Number): lambda: (iterable(lhs), iterable(rhs)),
        (Number, str): lambda: (str(lhs), rhs),
        (str, Number): lambda: (lhs, str(rhs))
    }.get(types, lambda: (iterable(lhs), iterable(rhs)))()

    return list(set(new_lhs) ^ set(new_rhs))
def set_intersection(lhs, rhs):
    # Why make my own function instead of using standard &? Because numbers and strings. that's why.
    types = VY_type(lhs), VY_type(rhs)
    new_lhs, new_rhs = {
        (Number, Number): lambda: (iterable(lhs), iterable(rhs)),
        (Number, str): lambda: (str(lhs), rhs),
        (str, Number): lambda: (lhs, str(rhs))
    }.get(types, lambda: (iterable(lhs), iterable(rhs)))()

    return list(set(new_lhs) & set(new_rhs))
def set_union(lhs, rhs):
    # Why make my own function instead of using standard |? Because numbers and strings. that's why.
    types = VY_type(lhs), VY_type(rhs)
    new_lhs, new_rhs = {
        (Number, Number): lambda: (iterable(lhs), iterable(rhs)),
        (Number, str): lambda: (str(lhs), rhs),
        (str, Number): lambda: (lhs, str(rhs))
    }.get(types, lambda: (iterable(lhs), iterable(rhs)))()

    return list(set(new_lhs) | set(new_rhs))
def sign_of(item):
    t = VY_type(item)
    if t == Number:
        if item < 0: return -1
        else: return [0, 1][item != 0]
    elif t is list:
        return vectorise(sign_of, item)
    else:
        return item
def split(haystack, needle, keep_needle=False):
    t_haystack = VY_type(haystack)
    if t_haystack in [Number, str]:
        haystack, needle = str(haystack), str(needle)
        if keep_needle:
            import re
            return re.split(f"({re.escape(needle)})", haystack) # I'm so glad Vyxal now uses built-in lists
        return haystack.split(needle)
    elif t_haystack is Generator:
        return split(haystack._dereference(), needle, keep_needle)
    else: #t_haystack is list
        ret = []
        temp = []
        for item in haystack:
            if item == needle:
                ret.append(temp)
                if keep_needle:
                    ret.append([needle])
                temp = []
            else:
                temp.append(item)
        if temp:
            ret.append(temp)
        return ret
def split_newlines_or_pow_10(item):
    return {
        Number: lambda: 10 ** item,
        str: lambda: item.split("\n")
    }.get(VY_type(item), lambda: vectorise(split_newlines_or_pow_10, item))()
def split_on_words(item):
    parts = []
    word = ""

    for char in item:
        if char not in string.ascii_letters:
            if word: parts.append(word)
            word = ""
            parts.append(char)
        else:
            word += char
    
    if word: parts.append(word)
    return parts
def string_empty(item):
    return {
        Number: lambda: item % 3,
        str: len(item) == 0
    }.get(VY_type(item), lambda: vectorise(string_empty, item))()
def strip_non_alphabet(name):
    stripped = filter(lambda char: char in string.ascii_letters + "_", name)
    return "".join(stripped)
def sublists(item):
    yield []
    length = len(item)
    for size in range(1, length + 1):
        for sub in range((length - size) + 1):
            yield item[sub:sub+size]
def substrings(item):
    for i in range(0, len(item) + 1):
        for j in range(1, len(item) + 1):
            yield item[i:j]
def subtract(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)

    return {
        (Number, Number): lambda: lhs - rhs,
        (str, str): lambda: lhs.replace(rhs, ""),
        (str, Number): lambda: lhs + ("-" * rhs),
        (Number, str): lambda: ("-" * lhs) + rhs,
        (list, types[1]): lambda: [subtract(item, rhs) for item in lhs],
        (types[0], list): lambda: [subtract(lhs, item) for item in rhs],
        (list, list): lambda: list(map(lambda x: subtract(*x), VY_zip(lhs, rhs))),
        (list, Generator): lambda: _two_argument(subtract, lhs, rhs),
        (Generator, list): lambda: _two_argument(subtract, lhs, rhs),
        (Generator, Generator): lambda: _two_argument(subtract, lhs, rhs)
    }.get(types, lambda: vectorise(subtract, lhs, rhs))()
def summate(vector):
    vector = iterable(vector)
    if type(vector) is Generator:
        return vector._reduce(add)
    ret = vector[0]
    for item in vector[1:]:
        ret = add(ret, item)
    return ret
def sums(vector):
    ret = []
    for i in range(len(vector)):
        ret.append(summate(vector[0:i+1]))
    return ret
tab = lambda x: NEWLINE.join(["    " + item for item in x.split(NEWLINE)]).rstrip("    ")
def transilterate(original, new, value):
    t_string = type(value)
    original = deref(original, True)
    if t_string == Generator:
        t_string = list
    ret = t_string()
    for char in value:
        if t_string is str: char = str(char)
        try:
            ind = original.index(char)
            ret += t_string(new[ind])
        except:
            ret += t_string(char)
    return ret
def transpose(vector):
    # https://github.com/DennisMitchell/jellylanguage/blob/70c9fd93ab009c05dc396f8cc091f72b212fb188/jelly/interpreter.py#L1311
    vector = iterable(vector); vector = list(vector)
    return Generator(map(lambda t: filter(None.__ne__, t), itertools.zip_longest(*map(iterable, vector))))
def trim(lhs, rhs, left = False, right = False):
    # I stole this from Jelly (but I overloaded it)
    #https://github.com/DennisMitchell/jellylanguage/blob/master/jelly/interpreter.py#L1131

    if type(rhs) is Function:
        lhs = iterable(lhs)
        def gen():
            for index, item in enumerate(lhs):
                if index % 2:
                    yield _safe_apply(rhs, item)
        return gen()

    if VY_type(lhs) == Number:
        lhs = str(lhs)
    if VY_type(rhs) == Number:
        rhs = str(rhs)
    lindex = 0
    rindex = len(lhs)
    if left:
        while lindex < rindex and rhs[lindex] in lhs:
            lindex += 1
    if right:
        while lindex < rindex and rhs[rindex - 1] in lhs:
            rindex -= 1
    return lhs[lindex:rindex]
def truthy_indexes(vector):
    ret = []
    for i in range(len(vector)):
        if bool(vector[i]):
            ret.append(i)
    return ret
def two_power(item):
    if VY_type(item) == Number: return 2 ** item
    elif VY_type(item) is str:
        out = ""
        for char in item:
            if char in string.ascii_letters:
                out += char
        return out
    else:
        return vectorise(two_power, item)
def uninterleave(item):
    left, right = [], []
    for i in range(len(item)):
        if i % 2 == 0: left.append(item[i])
        else: right.append(item[i])
    if type(item) is str:
        return ["".join(left), "".join(right)]
    return [left, right]
def uniquify(vector):
    seen = []
    for item in vector:
        if not item in seen:
            yield item
            seen.append(item)
def unsympy(item):
    if type(item) in (list, Generator): return vectorise(unsympy, item)
    if item.is_Integer: return int(item)
    elif item.is_Float: return float(item)
    else: return item
def urlify(item):
    if not (item.startswith("http://") or item.startswith("https://")):
        return "https://" + item
    return item
def vectorise(fn, left, right=None, third=None, explicit=False):
    if third:
        types = (VY_type(left), VY_type(right))
        def gen():
            for pair in VY_zip(left, right):
                yield _safe_apply(fn, *pair, third)
        
        def expl(l, r):
            for item in l:
                yield _safe_apply(fn, item, r, third)

        def swapped_expl(l, r):
            for item in r:
                yield _safe_apply(fn, l, item, third)

        return Generator({
            (types[0], types[1]): (lambda: _safe_apply(fn, iterable(left), right),
                                   lambda: expl(iterable(left), right)),
            (list, types[1]): (lambda: [_safe_apply(fn, x, right) for x in left],
                               lambda: expl(left, right)),
            (types[0], list): (lambda: [_safe_apply(fn, left, x) for x in right],
                               lambda: swapped_expl(left, right)),
            (Generator, types[1]): (lambda: expl(left, right),
                                    lambda: expl(left, right)),
            (types[0], Generator): (lambda: swapped_expl(left, right),
                                    lambda: swapped_expl(left, right)),
            (list, list): (lambda: gen(),
                           lambda: expl(left, right)),
            (Generator, Generator): (lambda: gen(),
                                     lambda: expl(left, right)),
            (list, Generator): (lambda: gen(),
                                lambda: expl(left, right)),
            (Generator, list): (lambda: gen(),
                                lambda: expl(left, right))
        }[types][explicit]())
    elif right:
        types = (VY_type(left), VY_type(right))

        def gen():
            for pair in VY_zip(left, right):
                yield _safe_apply(fn, *pair)
        
        def expl(l, r):
            for item in l:
                yield _safe_apply(fn, item, r)

        def swapped_expl(l, r):
            for item in r:
                yield _safe_apply(fn, l, item)
        return Generator({
            (types[0], types[1]): (lambda: _safe_apply(fn, iterable(left), right),
                                   lambda: expl(iterable(left), right)),
            (list, types[1]): (lambda: [_safe_apply(fn, x, right) for x in left],
                               lambda: expl(left, right)),
            (types[0], list): (lambda: [_safe_apply(fn, left, x) for x in right],
                               lambda: swapped_expl(left, right)),
            (Generator, types[1]): (lambda: expl(left, right),
                                    lambda: expl(left, right)),
            (types[0], Generator): (lambda: swapped_expl(left, right),
                                    lambda: swapped_expl(left, right)),
            (list, list): (lambda: gen(),
                           lambda: expl(left, right)),
            (Generator, Generator): (lambda: gen(),
                                     lambda: expl(left, right)),
            (list, Generator): (lambda: gen(),
                                lambda: expl(left, right)),
            (Generator, list): (lambda: gen(),
                                lambda: expl(left, right))
        }[types][explicit]())
            
    else:
        if VY_type(left) is Generator:
            def gen():
                for item in left:
                    yield _safe_apply(fn, item)
            return Generator(gen())
        elif VY_type(left) in (str, Number):
            return _safe_apply(fn, iterable(left))
        else:
            ret =  [_safe_apply(fn, x) for x in left]
            return ret
def vectorised_not(item):
    return {
        Number: lambda: int(not item),
        str: lambda: int(not item)
    }.get(VY_type(item), lambda: vectorise(vectorised_not, item))()
def vertical_join(vector, padding=" "):
    if VY_type(padding) == VY_type(vector) == Number:
        return abs(vector - padding)

    lengths = list(map(len, deref(vector, True)))
    vector = [padding * (max(lengths) - len(x)) + x for x in vector]

    out = ""
    for i in range(max(lengths)):
        for item in vector:
            out += item[i]
        out += "\n"

    return out
def wrap(vector, width):
    types = VY_type(vector), VY_type(width)
    if types == (Function, types[1]):
        return map_every_n(width, vector, 2)
    elif types == (types[0], Function):
        return map_every_n(vector, width, 2)

    # Because textwrap.wrap doesn't consistently play nice with spaces
    ret = []
    temp = []
    for item in vector:
        temp.append(item)
        if len(temp) == width:
            if all([type(x) is str for x in temp]):
                ret.append("".join(temp))
            else:
                ret.append(temp[::])
            temp = []
    if len(temp) < width and temp:
        if all([type(x) is str for x in temp]):
            ret.append("".join(temp))
        else:
            ret.append(temp[::])

    return ret
def VY_abs(item):
    return {
        Number: lambda: abs(item),
        str: lambda: remove(remove(remove(item, " "), "\n"), "\t"),
    }.get(VY_type(item), lambda: vectorise(VY_abs, item))()
def VY_bin(item):
    t_item = VY_type(item)
    return {
        Number: lambda: [int(x) for x in bin(int(item))[2:]],
        str: lambda: [[int (x) for x in bin(ord(let))[2:]] for let in item]
    }.get(t_item, lambda: vectorise(VY_bin, item))()
def VY_divmod(lhs, rhs):
    types = VY_type(lhs), VY_type(rhs)
    return {
        (Number, Number): lambda: [lhs // rhs, lhs % rhs],
        (types[0], Number): lambda: Generator(itertools.combinations(lhs, rhs)),
        (str, str): lambda: trim(lhs, rhs)
    }[types]()
def VY_eval(item):
    if VY_type(item) is Number: return 2 ** item
    elif VY_type(item) in [list, Generator]: return vectorise(VY_eval, item)
    if online_version or safe_mode:
        import regex
        pobj = regex.compile(r"""(\[(((-?\d+(\.\d+)?)|\g<1>|"[^"]*"|'[^']*')(, *)?)*\])|(-?\d+(\.\d+)?$)|"[^"]*"|'[^']*'""")
        mobj = pobj.match(item)
        if mobj:
            try:
                ret = eval(item)
                return ret
            except:
                return item
        else:
            return item
    else:
        try:
            ret = eval(item)
            return ret
        except:
            return item
def VY_exec(item):
    if VY_type(item) is str:
        exec(VY_compile(item))
        return []
    elif VY_type(item) == Number:
        return [divide(1, item)]
    else:
        return [vectorise(VY_exec, item)]
def VY_filter(fn, vector):
    def default_case(lhs, rhs):
        # remove elements from a that are in b
        out = "" if type(lhs) is str else []
        for item in lhs:
            if item not in rhs:
                if type(out) is str:
                    out += str(item)
                else:
                    out.append(item)
        return out
    
    def _filter(function, vec):
        for item in vec:
            val = function([item])[-1]
            if bool(val):
                yield item
    types = (VY_type(fn), VY_type(vector))
    return {
        types: lambda: default_case(iterable(fn, str), iterable(vector, str)),
        (Function, types[1]): lambda: Generator(_filter(fn, iterable(vector, range))),
        (types[0], Function): lambda: Generator(_filter(vector, iterable(fn, range)))

    }[types]()
def VY_int(item, base=10):
    t_item = type(item)
    if t_item not in [str, float, int, complex]:
        ret = 0
        for element in item:
            ret = multiply(ret, base)
            ret = add(ret, element)
        return ret
    elif t_item is str:
        return int(item, base)
    elif t_item is complex:
        return numpy.real(item)
    elif t_item:
        return VY_int(iterable(item), base)
def VY_map(fn, vector):
    ret = []
    t_vector = VY_type(vector)
    t_function = VY_type(fn)
    if not Function in (t_vector, t_function):
        def gen():
            for item in iterable(fn):
                yield [vector, item]
        return Generator(gen())
    
    vec, function = ((vector, fn), (fn, vector))[t_vector is Function]
    if VY_type(vec) == Number:
        vec = range(MAP_START, int(vec) + MAP_OFFSET)
    if VY_type(vec) is Generator:
        def gen():
            for item in vec:
                yield _safe_apply(function, item)
        return Generator(gen())
    for item in vec:
        result = function([item])
        ret.append(result[-1])
    return ret
def VY_max(item, *others):
    if others:
        biggest = item
        for sub in others:
            res = compare(deref(sub), deref(biggest), Comparitors.GREATER_THAN)
            if VY_type(res) in [list, Generator]:
                res = any(res)
            if res:
                biggest = sub
        return biggest
    else:
        item = flatten(item)
        if item:
            biggest = item[0]
            for sub in item[1:]:
                res = compare(deref(sub), deref(biggest), Comparitors.GREATER_THAN)
                if VY_type(res) in [list, Generator]:
                    res = any(res)
                if res:
                    biggest = sub
            return biggest
        return item
def VY_min(item, *others):
    if others:
        smallest = item
        for sub in others:
            res = compare(deref(sub), deref(smallest), Comparitors.LESS_THAN)
            if VY_type(res) in [list, Generator]:
                res = any(res)
            if res:
                smallest = sub
        return smallest
    else:
        item = flatten(item)
        if item:
            smallest = item[0]
            for sub in item[1:]:
                res = compare(deref(sub), deref(smallest), Comparitors.LESS_THAN)
                if VY_type(res) in [list, Generator]:
                    res = any(res)
                if res:
                    smallest = sub
            return smallest
        return item
def VY_oct(item):
    return {
        Number: lambda: oct(item)[2:],
        str: lambda: (lambda: item, lambda: oct(int(item)))[item.isnumeric()]()[2:]
    }.get(VY_type(item), lambda:vectorise(VY_oct, item))()
def VY_print(item, end="\n", raw=False):
    global output, printed
    printed = True
    t_item = type(item)
    if t_item is Generator:
        item._print(end)
    
    elif t_item is list:
        VY_print("⟨", "", False)
        if item:
            for value in item[:-1]:
                VY_print(value, "|", True)
            VY_print(item[-1], "", True)
        VY_print("⟩", end, False)
    else:
        if t_item is int and keg_mode:
            item = chr(item)
        if raw:
            if online_version:
                output[1] += VY_repr(item) + end
            else:
                print(VY_repr(item), end=end)
        else:
            if online_version:
                output[1] += VY_str(item) + end
            else:
                print(VY_str(item), end=end)
    if online_version and len(output) > ONE_TWO_EIGHT_KB:
        exit(code=1)
def VY_sorted(vector, fn=None):
    if fn is not None and type(fn) is not Function:
        return inclusive_range(vector, fn)
    t_vector = type(vector)
    vector = iterable(vector, str)
    if t_vector is Generator:
        vector = vector.gen
    if fn:
        sorted_vector = sorted(vector, key=lambda x: fn([x]))
    else:
        sorted_vector = sorted(vector)


    return {
        int: lambda: int("".join(map(str, sorted_vector))),
        float: lambda: float("".join(map(str, sorted_vector))),
        str: lambda: "".join(map(str, sorted_vector))
    }.get(t_vector, lambda: Generator(sorted_vector))()
def VY_range(item, start=0, lift_factor=0):
    t_item = VY_type(item)
    if t_item == Number:
        if item < 0:
            return range(start, int(item) + lift_factor, -1)
        return range(start, int(item) + lift_factor)
    return item
def VY_reduce(fn, vector):
    t_type = VY_type(vector)
    if type(fn) != Function:
        return [vector, vectorise(reverse, fn)]
    if t_type is Generator: return [Generator(vector)._reduce(fn)]
    if t_type is Number:
        vector = list(range(MAP_START, int(vector) + MAP_OFFSET))
    vector = vector[::-1]
    working_value = pop(vector)
    vector = vector[::-1]

    for item in vector:
        working_value = fn([working_value, item], arity=2)[-1]
    return [working_value]
def VY_repr(item):
    t_item = VY_type(item)
    return {
        Number: lambda x: str(x),
        list: lambda x: "⟨" + "|".join([str(VY_repr(y)) for y in x]) + "⟩",
        Generator: lambda x: VY_repr(x._dereference()),
        str: lambda x: "`" + x + "`",
        Function: lambda x: "@FUNCTION:" + x.__name__
    }[t_item](item)
def VY_round(item):
    t_item = VY_type(item)
    if t_item == Number:
        return round(item)

    elif t_item is str:
        return [item[n:] for n in range(len(item) - 1, -1, -1)]
    return vectorise(VY_round, item)
def VY_str(item):  
    t_item = VY_type(item)
    return {
        Number: lambda x: str(x),
        str: lambda x: x,
        list: lambda x: "⟨" + "|".join([VY_repr(y) for y in x]) + "⟩",
        Generator: lambda x: VY_str(x._dereference()),
        Function: lambda x: "@FUNCTION:" + x.__name__
    }[t_item](item)
def VY_type(item):
    ty = type(item)
    if ty in [int, float, complex]:
        return Number
    return ty
def VY_zip(lhs, rhs):
    ind = 0
    if type(lhs) in [list, str]: lhs = iter(lhs)
    if type(rhs) in [list, str]: rhs = iter(rhs)
    while True:
        exhausted = 0
        try:
            l = next(lhs)
        except:
            l = 0
            exhausted += 1

        try:
            r = next(rhs)
        except:
            r = 0
            exhausted += 1
        if exhausted == 2:
            break
        else:
            yield [l, r]

        ind += 1
def VY_zipmap(fn, vector):
    if type(fn) is not Function:
        return [fn, VY_zip(vector, vector)]
    t_vector = VY_type(vector)
    if t_vector is Generator:
        orig = copy.deepcopy(vector)
        new = VY_map(fn, vector)
        return Generator(orig.zip_with(new))
    if t_vector == Number:
        vector = range(MAP_START, int(vector) + MAP_OFFSET)

    ret = []
    for item in vector:
        ret.append([item, fn([item])[-1]])

    return [ret]

constants = {
    "A": "string.ascii_uppercase",
    "e": "math.e",
    "f": "'Fizz'",
    "b": "'Buzz'",
    "F": "'FizzBuzz'",
    "H": "'Hello, World!'",
    "h": "'Hello World'",
    "1": "1000",
    "2": "10000",
    "3": "100000",
    "4": "1000000",
    "5": "10000000",
    "a": "string.ascii_lowercase",
    "L": "string.ascii_letters",
    "d": "string.digits",
    "6": "'0123456789abcdef'",
    "^": "'0123456789ABCDEF'",
    "o": "string.octdigits",
    "p": "string.punctuation",
    "P": "string.printable",
    "w": "string.whitespace",
    "r": "string.digits + string.ascii_letters",
    "B": "string.ascii_uppercase + string.ascii_lowercase",
    "Z": "string.ascii_uppercase[::-1]",
    "z": "string.ascii_lowercase[::-1]",
    "l": "string.ascii_letters[::-1]",
    "i": "math.pi",
    "n": "math.nan",
    "t": "math.tau",
    "D": "date.today().isoformat()",
    "N": "[dt.now().hour, dt.now().minute, dt.now().second]",
    "ḋ": "date.today().strftime('%d/%m/%Y')",
    "Ḋ": "date.today().strftime('%m/%d/%y')",
    "ð": "[date.today().day, date.today().month, date.today().year]",
    "β": "'{}[]<>()'",
    "Ḃ": "'()[]{}'",
    "ß": "'()[]'",
    "ḃ": "'([{'",
    "≥": "')]}'",
    "≤": "'([{<'",
    "Π": "')]}>'",
    "v": "'aeiou'",
    "V": "'AEIOU'",
    "∨": "'aeiouAEIOU'",
    "⟇": "commands.codepage",
    "½": "[1, 2]",
    "ḭ": "2 ** 32",
    "+": "[1, -1]",
    "-": "[-1, 1]",
    "≈": "[0, 1]",
    "/": "'/\\\\'",
    "R": "360",
    "W": "'https://'",
    "℅": "'http://'",
    "↳": "'https://www.'",
    "²": "'http://www.'",
    '"': "16",
    "∴": "32",
    "…": "64",
    "¶": "512",
    "⁋": "1024",
    "¦": "2048",
    "Ṅ": "4096",
    "ṅ": "8192",
    "¡": "16384",
    "ε": "32768",
    "₴": "65536",
    "×": "2147483648",
    "⁰": "'bcfghjklmnpqrstvwxyz'",
    "¹": "'bcfghjklmnpqrstvwxz'",
    "•": "['qwertyuiop', 'asdfghjkl', 'zxcvbnm']",
    "Ṡ": "dt.now().second",
    "Ṁ": "dt.now().minute",
    "Ḣ": "dt.now().hour",
    "τ": "int(dt.now().strftime('%j'))",
    "ṡ": "time.time()",
    "□": "[[0,1],[1,0],[0,-1],[-1,0]]",
    "…": "[[0,1],[1,0]]",
    "¹": "[-1,0,1]",
}

def VY_compile(source, header=""):
    if not source: return header or "pass"
    source = VyParse.Tokenise(VyParse.group_two_bytes(VyParse.group_strings(source)))
    compiled = ""
    for token in source:
        NAME, VALUE = token[VyParse.NAME], token[VyParse.VALUE]
        # print(NAME, VALUE)
        if NAME == VyParse.NO_STMT:
            compiled += commands.command_dict.get(VALUE, "  ")[0]
        elif NAME == VyParse.INTEGER:
            compiled += f"stack.append({VALUE})"
        elif NAME == VyParse.STRING_STMT:
            import utilities
            value = VALUE[VyParse.STRING_CONTENTS].replace('"', "\\\"")
            if raw_strings:
                compiled += f"stack.append(\"{value}\")" + NEWLINE
            else:
                compiled += f"stack.append(\"{utilities.uncompress(value)}\")" + NEWLINE
        elif NAME == VyParse.CHARACTER:
            compiled += f"stack.append({repr(VALUE[0])})"
        elif NAME == VyParse.IF_STMT:
            true_branch = VALUE[VyParse.IF_ON_TRUE]
            true_branch = tab(VY_compile(true_branch))

            compiled += "_IF_condition = bool(pop(stack))" + NEWLINE
            compiled += "if _IF_condition:" + NEWLINE + true_branch

            if VyParse.IF_ON_FALSE in VALUE:
                false_branch = VALUE[VyParse.IF_ON_FALSE]
                false_branch = tab(VY_compile(false_branch))
                compiled += NEWLINE + "else:" + NEWLINE
                compiled += false_branch
        elif NAME == VyParse.FOR_STMT:
            loop_variable = "LOOP_" + _mangle(compiled)
            if VyParse.FOR_VARIABLE in VALUE:
                loop_variable = "VAR_" + strip_non_alphabet(VALUE[VyParse.FOR_VARIABLE])

            compiled += "for " + loop_variable + " in VY_range(pop(stack)):" + NEWLINE
            compiled += tab("context_level += 1") + NEWLINE
            compiled += tab("context_values.append(" + loop_variable + ")") + NEWLINE
            compiled += tab(VY_compile(VALUE[VyParse.FOR_BODY])) + NEWLINE
            compiled += tab("context_level -= 1") + NEWLINE
            compiled += tab("context_values.pop()")
        elif NAME == VyParse.WHILE_STMT:
            condition = "stack.append(1)"
            if VyParse.WHILE_CONDITION in VALUE:
                condition = VY_compile(VALUE[VyParse.WHILE_CONDITION])

            compiled += condition + NEWLINE
            compiled += "while pop(stack):" + NEWLINE
            compiled += tab(VY_compile(VALUE[VyParse.WHILE_BODY])) + NEWLINE
            compiled += tab(condition)
        elif NAME == VyParse.FUNCTION_STMT:
            if VyParse.FUNCTION_BODY not in VALUE:
                # Function call
                compiled += "stack += FN_" + VALUE[VyParse.FUNCTION_NAME] + "(stack)"
            else:
                function_information = VALUE[VyParse.FUNCTION_NAME].split(":")
                # This will either be a single name, or name and parameter information

                parameter_count = 0
                function_name = function_information[0]
                parameters = []

                if len(function_information) >= 2:
                    for parameter in function_information[1:]:
                        if parameter == "*":
                            # Variadic parameters
                            parameters.append(-1)
                        elif parameter.isnumeric():
                            # Fixed arity
                            parameters.append(int(parameter))
                            parameter_count += parameters[-1]
                        else:
                            # Named parameter
                            parameters.append(parameter)
                            parameter_count += 1

                compiled += "def FN_" + function_name + "(parameter_stack, arity=None):" + NEWLINE
                compiled += tab("global context_level, context_values, input_level, input_values, retain_items, printed") + NEWLINE
                compiled += tab("context_level += 1") + NEWLINE
                compiled += tab("input_level += 1") + NEWLINE
                compiled += tab(f"this_function = FN_{function_name}") + NEWLINE
                if parameter_count == 1:
                    # There's only one parameter, so instead of pushing it as a list
                    # (which is kinda rather inconvienient), push it as a "scalar"

                    compiled += tab("context_values.append(parameter_stack[-1])")
                elif parameter_count != -1:
                    compiled += tab(f"context_values.append(parameter_stack[:-{parameter_count}])")
                else:
                    compiled += tab("context_values.append(parameter_stack)")

                compiled += NEWLINE

                compiled += tab("parameters = []") + NEWLINE

                for parameter in parameters:
                    if parameter == -1:
                        compiled += tab("""arity = pop(parameter_stack)
if VY_type(arity) == Number:
    parameters += parameter_stack[-int(arity):]
else:
    parameters += [arity]
""")
                    elif parameter == 1:
                        compiled += tab("parameters.append(pop(parameter_stack))")
                    elif isinstance(parameter, int):
                        compiled += tab(f"parameters += pop(parameter_stack, {parameter})")
                    else:
                        compiled += tab("VAR_" + parameter + " = pop(parameter_stack)")
                    compiled += NEWLINE

                compiled += tab("stack = parameters[::]") + NEWLINE
                compiled += tab("input_values[input_level] = [stack[::], 0]") + NEWLINE
                compiled += tab(VY_compile(VALUE[VyParse.FUNCTION_BODY])) + NEWLINE
                compiled += tab("context_level -= 1; context_values.pop()") + NEWLINE
                compiled += tab("input_level -= 1") + NEWLINE
                compiled += tab("return stack")
        elif NAME == VyParse.LAMBDA_STMT:
            defined_arity = 1
            if VyParse.LAMBDA_ARGUMENTS in VALUE:
                lambda_argument = VALUE[VyParse.LAMBDA_ARGUMENTS]
                if lambda_argument.isnumeric():
                    defined_arity = int(lambda_argument)
            signature = _mangle(compiled)
            compiled += f"def _lambda_{signature}(parameter_stack, arity=-1, self=None):" + NEWLINE
            compiled += tab("global context_level, context_values, input_level, input_values, retain_items, printed") + NEWLINE
            compiled += tab("context_level += 1") + NEWLINE
            compiled += tab("input_level += 1") + NEWLINE
            compiled += tab(f"this_function = _lambda_{signature}") + NEWLINE
            compiled += tab("stored = False") + NEWLINE
            compiled += tab("if 'stored_arity' in dir(self): stored = self.stored_arity;") + NEWLINE
            compiled += tab(f"if arity != {defined_arity} and arity >= 0: parameters = pop(parameter_stack, arity); stack = parameters[::]") + NEWLINE
            compiled += tab("elif stored: parameters = pop(parameter_stack, stored); stack = parameters[::]") + NEWLINE
            if defined_arity == 1:
                compiled += tab(f"else: parameters = pop(parameter_stack); stack = [parameters]") + NEWLINE
            else:
                compiled += tab(f"else: parameters = pop(parameter_stack, {defined_arity}); stack = parameters[::]") + NEWLINE
            compiled += tab("context_values.append(parameters)") + NEWLINE
            compiled += tab("input_values[input_level] = [stack[::], 0]") + NEWLINE
            compiled += tab(VY_compile(VALUE[VyParse.LAMBDA_BODY])) + NEWLINE
            compiled += tab("ret = [pop(stack)]") + NEWLINE
            compiled += tab("context_level -= 1; context_values.pop()") + NEWLINE
            compiled += tab("input_level -= 1") + NEWLINE
            compiled += tab("return ret") + NEWLINE
            compiled += f"stack.append(_lambda_{signature})"
        elif NAME == VyParse.LIST_STMT:
            compiled += "temp_list = []" + NEWLINE
            for element in VALUE[VyParse.LIST_ITEMS]:
                if element:
                    compiled += "def list_item(parameter_stack):" + NEWLINE
                    compiled += tab("stack = parameter_stack[::]") + NEWLINE
                    compiled += tab(VY_compile(element)) + NEWLINE
                    compiled += tab("return pop(stack)") + NEWLINE
                    compiled += "temp_list.append(list_item(stack))" + NEWLINE
            compiled += "stack.append(temp_list[::])"
        elif NAME == VyParse.FUNCTION_REFERENCE:
            compiled += f"stack.append(FN_{VALUE[VyParse.FUNCTION_NAME]})"
        elif NAME == VyParse.CONSTANT_CHAR:
            compiled += f"stack.append({constants[VALUE]})"
        elif NAME == VyParse.VECTORISATION_CHAR:
            compiled += VY_compile("λ" + VALUE + ";") + NEWLINE
            m = [0, -1]
            if len(VALUE) == 1 and VALUE in commands.command_dict: m = commands.command_dict[VALUE]
            elif VALUE[1] in commands.math_command_dict: m = commands.math_command_dict[VALUE[1]]
            elif VALUE[1] in commands.string_command_dict: m = commands.string_command_dict[VALUE[1]]
            elif VALUE[1] in commands.list_command_dict: m = commands.list_command_dict[VALUE[1]]
            elif VALUE[1] in commands.misc_command_dict: m = commands.misc_command_dict[VALUE[1]]

            m = m[-1]
            if m == 0:
                compiled += "fn = pop(stack); stack += fn(stack)"
            elif m == 1:
                compiled += "fn = pop(stack); stack.append(vectorise(fn, pop(stack), explicit=True))"
            elif m == 2:
                compiled += "fn = pop(stack); rhs, lhs = pop(stack, 2); stack.append(vectorise(fn, lhs, rhs, explicit=True))"
            elif m == 3:
                compiled += "fn = pop(stack); other, rhs, lhs = pop(stack, 3); stack.append(vectorise(fn, lhs, rhs, other, explicit=True))"
        elif NAME == VyParse.CODEPAGE_INDEX:
            compiled += f"stack.append({commands.codepage.find(VALUE)} + 101)"
        elif NAME == VyParse.TWO_BYTE_MATH:
            compiled += commands.math_command_dict.get(VALUE, "  ")[0]
        elif NAME == VyParse.TWO_BYTE_STRING:
            compiled += commands.string_command_dict.get(VALUE, "  ")[0]
        elif NAME == VyParse.TWO_BYTE_LIST:
            compiled += commands.list_command_dict.get(VALUE, "  ")[0]
        elif NAME == VyParse.TWO_BYTE_MISC:
            compiled += commands.misc_command_dict.get(VALUE, "  ")[0]
        elif NAME == VyParse.SINGLE_SCC_CHAR:
            import utilities
            import encoding
            if -1 < utilities.to_ten(VALUE, encoding.compression) < len(words._words):
                compiled += f"stack.append({repr(words.extract_word(VALUE))})"
            else:
                compiled += f"stack.append({repr(VALUE)})"

        elif NAME == VyParse.VARIABLE_SET:
            compiled += "VAR_" + VALUE[VyParse.VARIABLE_NAME] + " = pop(stack)"
        elif NAME == VyParse.VARIABLE_GET:
            compiled += "stack.append(VAR_" + VALUE[VyParse.VARIABLE_NAME] + ")"
        elif NAME == VyParse.COMPRESSED_NUMBER:
            import utilities, encoding
            number = utilities.to_ten(VALUE[VyParse.COMPRESSED_NUMBER_VALUE],
             encoding.codepage_number_compress)
            compiled += f"stack.append({number})" + NEWLINE
        elif NAME == VyParse.COMPRESSED_STRING:
            import utilities, encoding
            value = utilities.to_ten(VALUE[VyParse.COMPRESSED_STRING_VALUE],
             encoding.codepage_string_compress)
            value = utilities.from_ten(value, utilities.base27alphabet)
            compiled += f"stack.append('{value}')" + NEWLINE
        elif NAME == VyParse.PARA_APPLY:
            compiled += "temp_stack = stack[::]" + NEWLINE
            compiled += commands.command_dict.get(VALUE[0], "  ")[0] + NEWLINE
            compiled += "def _para_lambda(stack):" + NEWLINE
            compiled += tab(commands.command_dict.get(VALUE[1], "  ")[0]) + NEWLINE
            compiled += tab("return stack") + NEWLINE
            compiled += "stack.append(_para_lambda(temp_stack)[-1])"
        elif NAME == VyParse.PARA_APPLY_COLLECT:
            compiled += "temp_stack = stack[::]" + NEWLINE
            compiled += commands.command_dict.get(VALUE[0], "  ")[0] + NEWLINE
            compiled += "def _para_lambda(stack):" + NEWLINE
            compiled += tab(commands.command_dict.get(VALUE[1], "  ")[0]) + NEWLINE
            compiled += tab("return stack") + NEWLINE
            compiled += "stack.append(_para_lambda(temp_stack)[-1])" + NEWLINE
            compiled += "rhs, lhs = pop(stack, 2); stack.append([lhs, rhs])"
        elif NAME == VyParse.REGISTER_MODIFIER:
            compiled += "stack.append(register)" + NEWLINE
            built_in = commands.command_dict[VALUE]
            if built_in[1] > 1:
                compiled += commands.command_dict["$"][0] + NEWLINE
            compiled += built_in[0] + NEWLINE
            compiled += "register = pop(stack)"
        elif NAME == VyParse.ONE_CHAR_FUNCTION_REFERENCE:
            compiled += VY_compile("λ" + str(commands.command_dict[VALUE][1]) + "|" + VALUE)
        elif NAME == VyParse.DONT_POP:
            compiled += "retain_items = True" + NEWLINE
            compiled += VY_compile(VALUE) + NEWLINE
            compiled += "retain_items = False"
        elif NAME == VyParse.CONDITIONAL_EXECUTION:
            compiled += "if bool(pop(stack)):" + NEWLINE
            compiled += tab(VY_compile(VALUE))
        compiled += NEWLINE
    return header + compiled

def execute(code, flags, input_list, output_variable):
    global stack, register, printed, output, MAP_START, MAP_OFFSET
    global _join, _vertical_join, use_encoding, input_level, online_version, raw_strings
    global inputs, reverse_args, keg_mode, number_iterable, this_function
    online_version = True
    output = output_variable
    output[1] = ""
    output[2] = ""
    flags = flags

    if input_list:
        eval_function = VY_eval
        if 'Ṡ' in flags: eval_function = str
        inputs = list(map(eval_function, input_list.split("\n")))

    if 'a' in flags:
        inputs = [inputs]

    if flags:
        if 'H' in flags:
            stack = [100]
        if 'M' in flags:
            MAP_START = 0

        if 'm' in flags:
            MAP_OFFSET = 0
        
        if 'Ṁ' in flags:
            MAP_START = 0
            MAP_OFFSET = 0

        if 'j' in flags:
            _join = True

        if 'L' in flags:
            _vertical_join = True

        if 'v' in flags:
            use_encoding = True
        
        if 'r' in flags:
            reverse_args = True
        
        if 'K' in flags:
            keg_mode = True
        
        if 'R' in flags:
            number_iterable = range

        if 'D' in flags:
            raw_strings = True
        
        if 'h' in flags:
            output[1] = """
ALL flags should be used as is (no '-' prefix)
\tH\tPreset stack to 100
\tj\tPrint top of stack joined by newlines on end of execution
\tL\tPrint top of stack joined by newlines (Vertically) on end of execution
\ts\tSum/concatenate top of stack on end of execution
\tM\tMake implicit range generation start at 0 instead of 1
\tm\tMake implicit range generation end at n-1 instead of n
\tv\tUse Vyxal encoding for input file
\tc\tOutput compiled code
\tf\tGet input from file instead of arguments
\ta\tTreat newline seperated values as a list
\td\tPrint deep sum of top of stack on end of execution
\tr\tMakes all operations happen with reverse arguments
\tS\tPrint top of stack joined by spaces on end of execution
\tC\tCentre the output and join on newlines on end of execution
\tO\tDisable implicit output
\tK\tEnable Keg mode (input as ordinal values and integers as characters when outputting)
\tl\tPrint length of top of stack on end of execution
\tG\tPrint the maximum item of the top of stack on end of execution
\tg\tPrint the minimum item of the top of the stack on end of execution
\tW\tPrint the entire stack on end of execution
\tṠ\tTreat all inputs as strings (usually obtainable by wrapping in quotations)
\tR\tTreat numbers as ranges if ever used as an iterable
\tD\tTreat all strings as raw strings (don't decompress strings)
\tṪ\tPrint the sum of the entire stack
\t5\tMake the interpreter timeout after 5 seconds
\tT\tMake the interpreter timeout after 10 seconds
\tb\tMake the interpreter timeout after 15 seconds
\tB\tMake the interpreter timeout after 30 seconds
\tṀ\tEquivalent to having both m and M flags
"""
            return
    input_values[0] = [inputs, 0]
    code = VY_compile(code, "global stack, register, printed, output, MAP_START, MAP_OFFSET, _join, _vertical_join, use_encoding, input_level, raw_strings, retain_items, reverse_args, this_function\n")
    context_level = 0
    if flags and 'c' in flags:
        output[2] = code

    try:
        exec(code, globals())
    except Exception as e:
        output[2] += "\n" + str(e.args[0])

    if not printed and ('O' not in flags):
        if flags and 's' in flags:
            VY_print(summate(pop(stack)))
        elif flags and 'd' in flags:
            VY_print(summate(flatten(pop(stack))))
        elif flags and 'Ṫ' in flags:
            VY_print(summate(stack))
        elif flags and 'S' in flags:
            VY_print(" ".join([str(n) for n in pop(stack)]))
        elif flags and 'C' in flags:
            VY_print("\n".join(centre(pop(stack))))
        elif flags and 'l' in flags:
            VY_print(len(pop(stack)))
        elif flags and 'G' in flags:
            VY_print(VY_max(pop(stack)))
        elif flags and 'g' in flags:
            VY_print(VY_min(pop(stack)))
        elif flags and 'W' in flags:
            VY_print(stack)
        elif _vertical_join:
            VY_print(vertical_join(pop(stack)))
        elif _join:
            VY_print("\n".join([str(n) for n in pop(stack)]))
        else:
            VY_print(pop(stack))


if __name__ == "__main__":
    ### Debugging area
    import sys
    file_location = ""
    flags = ""
    inputs = []
    header = "stack = []\nregister = 0\nprinted = False\n"

    if len(sys.argv) > 1:
        file_location = sys.argv[1]
    if len(sys.argv) > 2:
        flags = sys.argv[2]
        if flags:
            eval_function = VY_eval
            if 'Ṡ' in flags:
                eval_function = str
            if 'H' in flags:
                stack = [100]
            if 'f' in flags:
                inputs = list(map(eval_function, open(sys.argv[3]).readlines()))
            else:
                inputs = list(map(eval_function,sys.argv[3:]))

        if 'a' in flags:
            inputs = [inputs]
        
    if not file_location: #repl mode

        while 1:
            line = input(">>> ")
            context_level = 0
            line = VY_compile(line, header)
            exec(line)
            VY_print(stack)
    elif file_location == "h":
        print("\nUsage: python3 Vyxal.py <file> <flags (single string of flags)> <input(s) (if not from STDIN)>")
        print("ALL flags should be used as is (no '-' prefix)")
        print("\tH\tPreset stack to 100")
        print("\tj\tPrint top of stack joined by newlines")
        print("\tL\tPrint top of stack joined by newlines (Vertically)")
        print("\ts\tSum/concatenate top of stack on end of execution")
        print("\tM\tMake implicit range generation start at 0 instead of 1")
        print("\tm\tMake implicit range generation end at n-1 instead of n")
        print("\tv\tUse Vyxal encoding for input file")
        print("\tc\tOutput compiled code")
        print("\tf\tGet input from file instead of arguments")
        print("\ta\tTreat newline seperated values as a list")
        print("\td\tDeep sum of top of stack")
        print("\tr\tMakes all operations happen with reverse arguments")
        print("\tS\tPrint top of stack joined by spaces")
        print("\tC\tCentre the output and join on newlines")
        print("\tO\tDisable implicit output")
        print("\tK\tEnable Keg mode")
        print("\tE\tEnable safe evaluation (offline interpreter only)")
        print("\tl\tPrint length of top of stack")
        print("\tG\tPrint the maximum item of the top of stack on end of execution")
        print("\tg\tPrint the minimum item of the top of the stack on end of execution")
        print("\tW\tPrint the entire stack on end of execution")
        print("\tṠ\tTreat all inputs as strings")
        print("\tR\tTreat numbers as ranges if ever used as an iterable")
        print("\tD\tTreat all strings as raw strings (don't decompress strings)")
        print("\tṪ\tPrint the sum of the entire stack")
        print("\tṀ\tEquivalent to having both m and M flags")
    else:
        if flags:
            if 'M' in flags:
                MAP_START = 0

            if 'm' in flags:
                MAP_OFFSET = 0
            
            if 'Ṁ' in flags:
                MAP_START = 0
                MAP_OFFSET = 0

            if 'j' in flags:
                _join = True

            if 'L' in flags:
                _vertical_join = True

            if 'v' in flags:
                use_encoding = True
            
            if 'r' in flags:
                reverse_args = True
            
            if 'K' in flags:
                keg_mode = True
            
            if 'E' in flags:
                safe_mode = True
            
            if 'H' in flags:
                header = "stack = [100]\nregister = 0\nprinted = False\n"
            
            if 'R' in flags:
                number_iterable = range

            if 'D' in flags:
                raw_strings = True

        # Encoding method thanks to Adnan (taken from the old 05AB1E interpreter)
        if use_encoding:
            import encoding
            code = open(file_location, "rb").read()
            code = encoding.vyxal_to_utf8(code)
        else:
            code = open(file_location, "r", encoding="utf-8").read()
        input_values[0] = [inputs, 0]
        code = VY_compile(code, header)
        context_level = 0
        if flags and 'c' in flags:
            print(code)
        exec(code)

        if not printed and ("O" not in flags):
            if flags and 's' in flags:
                print(summate(pop(stack)))
            elif flags and 'd' in flags:
                print(summate(flatten(pop(stack))))
            elif flags and 'Ṫ' in flags:
                VY_print(summate(stack))
            elif flags and "S" in flags:
                print(" ".join([VY_str(n) for n in pop(stack)]))
            elif flags and "C" in flags:
                print("\n".join(centre(pop(stack))))
            elif flags and "l" in flags:
                print(len(pop(stack)))
            elif flags and "G" in flags:
                print(VY_max(pop(stack)))
            elif flags and "g" in flags:
                print(VY_min(pop(stack)))
            elif flags and "W" in flags:
                print(VY_str(stack))
            elif _vertical_join:
                print(vertical_join(pop(stack)))
            elif _join:
                print("\n".join([VY_str(n) for n in pop(stack)]))
            else:
                VY_print(pop(stack))
