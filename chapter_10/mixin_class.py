class PrettyMixin:
    def dump(self):
        import pprint

        pprint.pprint(vars(self))


class Thing(PrettyMixin):
    pass


t = Thing()
t.name = "nyarlathotep"
t.feature = "ichor"
t.age = "eldritch"
t.dump()
