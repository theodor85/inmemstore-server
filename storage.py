

class Storage:

    _STORE = dict()

    def bulk_update(self, input_dict: dict):
        self._STORE.update(input_dict)
        return 201  # created

    def list(self):
        return self._STORE

    def delete(self, key) -> int:
        try:
            del self._STORE[key]
        except KeyError:
            return 404  # not found
        else:
            return 204  # No Content (success)

    def clear(self):
        self._STORE.clear()
        return 204  # No Content (success)
