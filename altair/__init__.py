__version__ = '1.0.dev0'

from .api import (
    load_vegalite_spec,
    Label,
    Formula,
    StackOffset,
    Data,
    FacetScaleConfig,
    AxisConfig,
    Shape,
    Axis,
    AggregateOp,
    ScaleConfig,
    NiceTime,
    Transform,
    VerticalAlign,
    SortOrder,
    Legend,
    LegendConfig,
    Column,
    FontWeight,
    SortField,
    Text,
    MarkConfig,
    TimeUnit,
    FacetConfig,
    FontStyle,
    Config,
    Order,
    HorizontalAlign,
    Path,
    Scale,
    Encoding,
    Size,
    FacetGridConfig,
    Row,
    Bin,
    AxisOrient,
    X, Y,
    Color,
    DataFormat,
    Chart,
    LayeredChart,
    FacetedChart,
    CellConfig,
    Detail,
)

from .datasets import (
    list_datasets,
    load_dataset
)
