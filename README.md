# Workflow Data Structure Utilities



## Getting started

This repo contains utilities which assist in manipulating data structures in workflow systems.  To be used along other workflow system capabilities, these Lambdas augment low-friction configuration and allow for focusing on implementation details.  Based on experience building hundreds of workflows, these are the most useful and commonly-needed functions.  They are all pure Python with an average of 99% coverage:

| **Function**                                      | **Description**                                                                                                                                                            | **Sample Payload**                                                           | **Response**           |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|------------------------|
| [ensure-list](./src/ensure-list/)                 | Takes an item which may be a list, and wraps it in a list if it is not.  Otherwise, returned as-is; useful for Map operations over data with structures you can't control. | `{"parameters": {"data": "a"}}`                                              | `["a"]`                |
| [find-and-replace](./src/find-and-replace/)       | Implements string substitution, using a needle, haystack, and replacement.                                                                                                 | `{"parameters": {"needle":"foobar", "haystack": "foo", "replacement": "-"}}` | `{"value": "-bar"}`    |
| [merge-list-of-dicts](./src/merge-list-of-dicts/) | Takes a list of dictionaries (commonly, results from a Map or Parallel operation) and combines them into a single dictionary.                                              | `{"parameters": {"data": [{"a": "b"}, {"c": "d"}]}}`                         | `{"a": "b", "c": "d"}` |


## Testing

Once you have cloned this repository, you will need [Coverage](https://coverage.readthedocs.io/) and [pytest](https://docs.pytest.org/) installed.  You can then run the `run_all_tests.sh` script to have tests executed for you, or check Gitlab.

```shell
pip install coverage pytest
./run_all_tests.sh
```

## Usage
Simply copy the relevant functions into your project and use the Lambda build method of your choice.  Being pure Python, most build/deploy methods should work out of the box.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.


