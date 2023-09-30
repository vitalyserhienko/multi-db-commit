import argparse

from strategies.common_session import create_users_combined_session
from strategies.context_manager import create_users_context_manager_session
from strategies.current import create_users_current


_strategies = {
    1: create_users_combined_session,
    2: create_users_context_manager_session,
    3: create_users_current
}

_options = [f"{k}: {v.__name__}" for (k, v) in _strategies.items()]


parser = argparse.ArgumentParser()
parser.add_argument(
    "-s", "--strategy", help=", ".join(_options), type=int,
)
args = parser.parse_args()

if __name__ == "__main__":
    try:
        _strategies[args.strategy]()
    except KeyError:
        print(f"Chose one of possible options: {', '.join(_options)}")
