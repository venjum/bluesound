"""
Bluesound Subscription module
Bluesound class requires set (list) of SubscriptionObject as argument for subscription_list
"""

# When for example skipping song, The Bluesound player can output information we don't want.
# Thus this is a default ignore list for all SubscriptionObjects
DEFAULT_IGNORE_VALUES = {'Spotify', 'None', None}


def lookup(dic, key, *keys):
    """
    Lookup key and keys in dictionary.

    Note:
        Can use function like this lookup(dict, *[key1, key2, key3])

    Return:
        Dictionary value or None if not found.
    """
    if keys:
        return lookup(dic.get(key, {}), *keys)
    return dic.get(key)


class SubscriptionObject:
    """
    Class for making a subscription object.
    Bluesound class requires set (list) of this class as argument for subscription_list
    """
    def __init__(self, keys, callback=None, ignore_values=DEFAULT_IGNORE_VALUES):
        """
        Initialize Subscription class

        arguments:
            keys: List of keys that will be used to access value in updateValue(dict)
            callback: Function that is called with new value if changed.
            ignore_values: Set of values that are not considered as  a new valid value.
        """
        self._keys = keys
        self._current_value = None
        self._callback = callback
        self._ignore_values = ignore_values

    def updateValue(self, dict):
        """
        Update self._current_value if value have changed and report this back to application in form of the given callback.
        """
        next_value = lookup(dict, *self._keys)
        if next_value != self._current_value and next_value not in self._ignore_values:
            self._current_value = next_value
            if self._callback is not None:
                self._callback(self._current_value)

    def setCallback(self, callback):
        """
        Set a callback after object have been made.
        """
        self._callback = callback

    def getValue(self):
        """
        Get current value store in object.
        """
        return self._current_value
