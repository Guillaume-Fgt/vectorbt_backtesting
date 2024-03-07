import sys
from streamlit.web import cli as stcli
from streamlit import runtime
from webapp import main


if __name__ == "__main__":
    if runtime.exists():
        main()
    else:
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())
