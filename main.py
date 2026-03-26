import json
import random
import datetime
from typing import Dict, List, Tuple

class CarAssistantEvaluator:
    """智能购车助手评测器"""
    
    def __init__(self):
        # 模拟测试集：真实用户query示例
        self.test_queries = [
            "20万左右适合家用的SUV推荐",
            "特斯拉Model 3和比亚迪汉怎么选",
            "省油耐用的轿车有哪些",
            "北京新能源车牌政策是什么",
            "宝马X5最新优惠多少",
            "安全性能最好的国产车",
            "适合女生开的自动挡小车",
            "混动和纯电动哪个更划算",
            "汽车保养一般多久一次",
            "二手车购买注意事项"
        ]
        
        # 模拟意图分类
        self.intent_categories = {
            "车型推荐": ["推荐", "哪些", "什么车"],
            "车型对比": ["对比", "怎么选", "哪个好"],
            "价格咨询": ["价格", "优惠", "多少钱"],
            "政策咨询": ["政策", "牌照", "补贴"],
            "保养维护": ["保养", "维修", "保险"]
        }
        
        # 模拟两种Prompt策略
        self.prompt_strategies = {
            "strategy_a": "简单直接回答用户问题",
            "strategy_b": "详细分析需求后给出个性化建议"
        }
        
        self.results = []
    
    def simulate_llm_response(self, query: str, strategy: str) -> Dict:
        """模拟大模型响应"""
        # 模拟意图识别
        intent = self._recognize_intent(query)
        
        # 根据策略模拟不同质量的回答
        if strategy == "strategy_a":
            accuracy = random.uniform(0.7, 0.85)  # 策略A准确率较低
            response = f"简单回答：关于'{query}'，建议您查看相关车型。"
        else:
            accuracy = random.uniform(0.85, 0.95)  # 策略B准确率较高
            response = f"详细分析：针对您的需求'{query}'，经过分析推荐以下方案..."
        
        # 模拟用户满意度（与准确率相关但有随机性）
        satisfaction = min(accuracy + random.uniform(-0.1, 0.1), 1.0)
        
        return {
            "query": query,
            "intent": intent,
            "strategy": strategy,
            "response": response,
            "accuracy": round(accuracy, 3),
            "satisfaction": round(satisfaction, 3),
            "timestamp": datetime.datetime.now().isoformat()
        }
    
    def _recognize_intent(self, query: str) -> str:
        """模拟意图识别"""
        for intent, keywords in self.intent_categories.items():
            for keyword in keywords:
                if keyword in query:
                    return intent
        return "其他"
    
    def run_ab_test(self, num_tests: int = 20) -> Dict:
        """运行AB测试对比两种策略"""
        print("开始AB测试...")
        print(f"测试样本数：{num_tests}")
        print("-" * 50)
        
        for i in range(num_tests):
            query = random.choice(self.test_queries)
            strategy = random.choice(["strategy_a", "strategy_b"])
            
            result = self.simulate_llm_response(query, strategy)
            self.results.append(result)
            
            # 打印测试进度
            if (i + 1) % 5 == 0:
                print(f"已完成 {i + 1}/{num_tests} 次测试")
        
        return self._analyze_results()
    
    def _analyze_results(self) -> Dict:
        """分析测试结果"""
        strategy_a_results = [r for r in self.results if r["strategy"] == "strategy_a"]
        strategy_b_results = [r for r in self.results if r["strategy"] == "strategy_b"]
        
        def calculate_metrics(results: List) -> Dict:
            if not results:
                return {"count": 0, "avg_accuracy": 0, "avg_satisfaction": 0}
            
            return {
                "count": len(results),
                "avg_accuracy": round(sum(r["accuracy"] for r in results) / len(results), 3),
                "avg_satisfaction": round(sum(r["satisfaction"] for r in results) / len(results), 3)
            }
        
        metrics_a = calculate_metrics(strategy_a_results)
        metrics_b = calculate_metrics(strategy_b_results)
        
        # 计算提升比例
        accuracy_improvement = round(
            (metrics_b["avg_accuracy"] - metrics_a["avg_accuracy"]) / metrics_a["avg_accuracy"] * 100, 1
        ) if metrics_a["avg_accuracy"] > 0 else 0
        
        return {
            "strategy_a": metrics_a,
            "strategy_b": metrics_b,
            "accuracy_improvement": f"{accuracy_improvement}%",
            "total_tests": len(self.results),
            "test_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def generate_report(self, analysis: Dict):
        """生成评测报告"""
        print("\n" + "=" * 50)
        print("智能购车助手AI评测报告")
        print("=" * 50)
        
        print(f"\n📊 测试概况：")
        print(f"   总测试次数：{analysis['total_tests']}")
        print(f"   测试时间：{analysis['test_time']}")
        
        print(f"\n🔍 策略A效果（{self.prompt_strategies['strategy_a']}）：")
        print(f"   样本数量：{analysis['strategy_a']['count']}")
        print(f"   意图识别准确率：{analysis['strategy_a']['avg_accuracy']:.1%}")
        print(f"   用户满意度：{analysis['strategy_a']['avg_satisfaction']:.1%}")
        
        print(f"\n🚀 策略B效果（{self.prompt_strategies['strategy_b']}）：")
        print(f"   样本数量：{analysis['strategy_b']['count']}")
        print(f"   意图识别准确率：{analysis['strategy_b']['avg_accuracy']:.1%}")
        print(f"   用户满意度：{analysis['strategy_b']['avg_satisfaction']:.1%}")
        
        print(f"\n📈 效果提升：")
        print(f"   准确率提升：{analysis['accuracy_improvement']}")
        
        print(f"\n💡 迭代建议：")
        if float(analysis['accuracy_improvement'].replace('%', '')) > 10:
            print("   1. 推荐采用策略B的Prompt设计")
            print("   2. 在详细分析用户需求方面继续优化")
            print("   3. 扩大测试样本覆盖更多场景")
        else:
            print("   1. 需要进一步优化Prompt策略")
            print("   2. 分析具体失败案例进行针对性改进")
        
        print("\n" + "=" * 50)

def main():
    """主函数"""
    print("🚗 智能购车助手AI评测系统")
    print("模拟真实购车场景下的AI助手评测流程")
    print("=" * 50)
    
    # 初始化评测器
    evaluator = CarAssistantEvaluator()
    
    # 运行AB测试
    analysis = evaluator.run_ab_test(num_tests=20)
    
    # 生成评测报告
    evaluator.generate_report(analysis)
    
    # 保存结果到文件（模拟数据归因分析）
    with open("evaluation_results.json", "w", encoding="utf-8") as f:
        json.dump(evaluator.results, f, ensure_ascii=False, indent=2)
    
    print("\n✅ 评测完成！结果已保存至 evaluation_results.json")

if __name__ == "__main__":
    main()