状态图与简单类图
负责人：Wangjh-2004（成员B）。 两张图均使用 Mermaid 绘制，完整可渲染的代码块即图的源文件（见 docs/assets/README.md 的约定），不再上传同内容图片。 工单创建后进入“待处理”，只有“开始维修”后进入“处理中”，只有“完成维修”后进入“已完成”。本实验没有重新打开、取消、跳过处理中等操作，图中不出现这些状态或转换。

状态图
stateDiagram-v2
    state "待处理" as PENDING
    state "处理中" as PROCESSING
    state "已完成" as COMPLETED
    [*] --> PENDING : 创建工单
    PENDING --> PROCESSING : 开始维修
    PROCESSING --> COMPLETED : 完成维修
    COMPLETED --> [*]

状态说明
中文状态  程序英文值      含义
待处理   	PENDING	    工单创建后的初始状态
处理中   	PROCESSING	维护人员已开始维修
已完成	    COMPLETED	  维修结束，工单生命周期终止

转换规则
允许的转换只有两条：待处理 PENDING → 处理中 PROCESSING（操作“开始维修”）、处理中 PROCESSING → 已完成 COMPLETED（操作“完成维修”）。
其余转换一律拒绝，包括：待处理直接转已完成、已完成退回处理中、同一状态转回自己。
本实验没有重新打开、取消、跳过处理中等操作，因此状态图中没有这些状态或转换。

简单类图
classDiagram
    class Device {
        +String deviceId
        +String name
        +String location
    }
    class WorkOrder {
        +String orderId
        +String deviceId
        +String description
        +String status
    }
    Device "1" -- "0..*" WorkOrder : 产生工单

属性与关系说明
Device 表示设备，至少包含 deviceId（设备编号）、name（设备名称）、location（安装位置）。
WorkOrder 表示工单，至少包含 orderId（工单编号）、deviceId（对应设备编号）、description（故障描述）、status（工单状态）。
一台设备可以有 0 到多张工单；每张工单必须对应 1 台设备，通过 WorkOrder 中的 deviceId 关联。
类图只描述数据结构关系；工单的生命周期画在上面的状态图中，两种图不混为一张。

与需求的一致性检查
- [x]中文状态与程序英文值对应：待处理/PENDING、处理中/PROCESSING、已完成/COMPLETED
- [x]只允许两条转换：待处理转处理中、处理中转已完成，其余拒绝
- [x]一台设备与多张工单关系清楚：1 台设备对应 0..* 张工单，每张工单对应 1 台设备


    
