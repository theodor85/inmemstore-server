from typing import Union, Any, MutableSequence, List, Tuple, Dict


class Storage:

    _STORE: Dict[Any, Any] = dict()

    def bulk_update(self, input_dict: dict):
        self._STORE.update(input_dict)
        return 201  # created

    def list(self):
        return self._STORE

    def get_value(self, key):
        status_code = 200
        try:
            value = self._STORE[key]
        except KeyError:
            status_code = 404  # not found
            value = None
        else:
            status_code = 200  # OK
        return value, status_code

    def delete(self, keys: Union[Any, MutableSequence]) -> Tuple[List, int]:
        status_code = 204
        if isinstance(keys, MutableSequence):
            result_list = list()
            for item in keys:
                try:
                    del self._STORE[item]
                except KeyError:
                    result_list.append({item: 'Item not found'})
                else:
                    result_list.append({item: 'Item has been deleted'})
            return result_list, status_code
        else:
            try:
                del self._STORE[keys]
            except KeyError:
                status_code = 404  # not found
            else:
                status_code = 204  # No Content (success)
            return [], status_code

    def clear(self):
        self._STORE.clear()
        return 204  # No Content (success)
