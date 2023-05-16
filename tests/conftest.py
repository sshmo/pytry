"""pytest entry config file."""

from pathlib import Path

import pytest
from pyinstrument import Profiler

TESTS_ROOT = Path.cwd()


@pytest.fixture(autouse=True)
def auto_profile(request):
    """Profiling fixture from pyinstrument for profiling tests."""
    PROFILE_ROOT = TESTS_ROOT / ".profiles"
    # Turn profiling on
    profiler = Profiler()
    profiler.start()

    yield  # Run test

    profiler.stop()
    PROFILE_ROOT.mkdir(exist_ok=True)
    results_file = PROFILE_ROOT / f"{request.node.name}.html"
    with open(results_file, "w", encoding="utf-8") as f_html:
        f_html.write(profiler.output_html())
